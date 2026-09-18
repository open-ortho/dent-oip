"""Generate exact vector diagrams for orthodontic viewset layouts."""

import csv
import logging
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path


logging.basicConfig(level=logging.INFO)

PATH_ROOT = Path(__file__).resolve().parent.parent
PATH_OUTPUT = PATH_ROOT / "source" / "images-static" / "generated"
PATH_LAYOUTS = PATH_ROOT / "source" / "tables" / "viewset_layouts"


@dataclass(frozen=True)
class CommonGeometry:
    """Scale-independent dimensions established by the VS-01 layout."""

    reference_viewset: str
    reference_width: Decimal
    horizontal_margin: Decimal
    vertical_margin: Decimal
    horizontal_gap: Decimal
    vertical_gap: Decimal
    box_aspect_ratios: dict[str, Decimal]


@dataclass(frozen=True)
class RowDefinition:
    """A top-to-bottom row in a viewset layout."""

    box_count: int
    first_number: int
    row_type: str


@dataclass(frozen=True)
class LayoutDefinition:
    """A viewset arrangement using the common VS-01 physical geometry."""

    name: str
    rows: tuple[RowDefinition, ...]
    geometry: CommonGeometry
    box_width: Decimal

    @property
    def width(self) -> Decimal:
        max_columns = max(row.box_count for row in self.rows)
        return (
            2 * self.geometry.horizontal_margin
            + max_columns * self.box_width
            + (max_columns - 1) * self.geometry.horizontal_gap
        )

    @property
    def height(self) -> Decimal:
        row_heights = sum(
            self.box_width / self.geometry.box_aspect_ratios[row.row_type]
            for row in self.rows
        )
        return (
            2 * self.geometry.vertical_margin
            + (len(self.rows) - 1) * self.geometry.vertical_gap
            + row_heights
        )

    @property
    def height_ratio(self) -> Decimal:
        return self.height / self.width


@dataclass(frozen=True)
class Box:
    """A box in common physical layout units."""

    number: int
    left: Decimal
    bottom: Decimal
    width: Decimal
    height: Decimal


def _decimal(value: str) -> Decimal:
    if "/" in value:
        numerator, denominator = value.split("/", maxsplit=1)
        return Decimal(numerator) / Decimal(denominator)
    return Decimal(value)


def load_geometry(path: Path) -> CommonGeometry:
    """Load the common geometry derived from VS-01."""
    with path.open(encoding="utf-8", newline="") as input_file:
        values = {
            record["Parameter"]: record["Value"]
            for record in csv.DictReader(input_file)
        }
    box_aspect_ratios = {
        row_type: _decimal(values[f"{row_type} Box Width:Height"])
        for row_type in ("Top", "Middle", "Bottom")
    }
    return CommonGeometry(
        reference_viewset=values["Reference Viewset"],
        reference_width=_decimal(values["Reference Layout Width"]),
        horizontal_margin=_decimal(values["Horizontal Margin"]),
        vertical_margin=_decimal(values["Vertical Margin"]),
        horizontal_gap=_decimal(values["Horizontal Gap"]),
        vertical_gap=_decimal(values["Vertical Gap"]),
        box_aspect_ratios=box_aspect_ratios,
    )


def load_rows(path: Path, geometry: CommonGeometry) -> tuple[RowDefinition, ...]:
    """Load one viewset's row arrangement."""
    with path.open(encoding="utf-8", newline="") as input_file:
        records = list(csv.DictReader(input_file))
    if not records:
        raise ValueError(f"No rows defined in {path}")

    rows = tuple(
        RowDefinition(
            box_count=int(record["Boxes"]),
            first_number=int(record["First ILC"]),
            row_type=record["Row Type"],
        )
        for record in records
    )
    for row in rows:
        if row.row_type not in geometry.box_aspect_ratios:
            raise ValueError(f"Unknown row type {row.row_type} in {path}")
    return rows


def load_layouts(path: Path = PATH_LAYOUTS) -> tuple[LayoutDefinition, ...]:
    """Load all arrangements and calculate the canonical VS-01 box width."""
    geometry = load_geometry(path / "geometry.csv")
    arrangements = {
        layout_path.stem: load_rows(layout_path, geometry)
        for layout_path in sorted(path.glob("VS-*.csv"))
    }
    reference_rows = arrangements[geometry.reference_viewset]
    reference_columns = max(row.box_count for row in reference_rows)
    box_width = (
        geometry.reference_width
        - 2 * geometry.horizontal_margin
        - (reference_columns - 1) * geometry.horizontal_gap
    ) / reference_columns

    return tuple(
        LayoutDefinition(
            name=name,
            rows=rows,
            geometry=geometry,
            box_width=box_width,
        )
        for name, rows in arrangements.items()
    )


LAYOUTS = load_layouts()


def calculate_boxes(layout: LayoutDefinition) -> tuple[Box, ...]:
    """Lay out boxes in common physical units before normalization."""
    boxes = []
    bottom = layout.geometry.vertical_margin
    row_heights = tuple(
        layout.box_width / layout.geometry.box_aspect_ratios[row.row_type]
        for row in layout.rows
    )
    for row, row_height in reversed(tuple(zip(layout.rows, row_heights))):
        row_width = (
            row.box_count * layout.box_width
            + (row.box_count - 1) * layout.geometry.horizontal_gap
        )
        left = (layout.width - row_width) / 2
        for index in range(row.box_count):
            boxes.append(
                Box(
                    number=row.first_number + index,
                    left=left
                    + index * (layout.box_width + layout.geometry.horizontal_gap),
                    bottom=bottom,
                    width=layout.box_width,
                    height=row_height,
                )
            )
        bottom += row_height + layout.geometry.vertical_gap

    return tuple(sorted(boxes, key=lambda box: box.number))


def _number(value: Decimal) -> str:
    return f"{value:.3f}"


def render_svg(layout: LayoutDefinition) -> str:
    """Render a self-contained SVG with normalized coordinate labels."""
    layout_left = Decimal(60)
    layout_top = Decimal(80)
    layout_width = layout.width
    layout_height = layout.height
    page_width = layout_left + layout_width + Decimal(180)
    page_height = layout_top + layout_height + Decimal(100)
    dimension_x = layout_left + layout_width + Decimal(45)
    dimension_label_x = layout_left + layout_width + Decimal(105)
    note_y = layout_top + layout_height + Decimal(60)
    boxes = calculate_boxes(layout)

    elements = []
    for box in boxes:
        x = layout_left + box.left
        y = layout_top + layout_height - box.bottom - box.height
        left = box.left / layout_width
        right = (box.left + box.width) / layout_width
        bottom = box.bottom / layout_height
        top = (box.bottom + box.height) / layout_height
        elements.append(
            f'''  <g>
    <rect class="box" x="{x:.3f}" y="{y:.3f}" width="{box.width:.3f}" height="{box.height:.3f}"/>
    <circle class="corner" cx="{x:.3f}" cy="{y:.3f}" r="7"/>
    <circle class="corner" cx="{x + box.width:.3f}" cy="{y + box.height:.3f}" r="7"/>
    <text class="coordinate" x="{x + 10:.3f}" y="{y + 24:.3f}">({_number(left)}, {_number(top)})</text>
    <text class="coordinate" x="{x + box.width - 10:.3f}" y="{y + box.height - 10:.3f}" text-anchor="end">({_number(right)}, {_number(bottom)})</text>
    <text class="number" x="{x + box.width / 2:.3f}" y="{y + box.height / 2:.3f}">{box.number}</text>
  </g>'''
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{page_width:.3f}" height="{page_height:.3f}"
     viewBox="0 0 {page_width:.3f} {page_height:.3f}" role="img"
     aria-labelledby="title description">
  <title id="title">{layout.name} normalized layout</title>
  <desc id="description">
    Boxes are assembled in common VS-01 physical units, then normalized to the
    resulting layout width and height. The normalized layout ratio is
    1.000 to {_number(layout.height_ratio)}.
  </desc>
  <defs>
    <marker id="arrow-start" markerWidth="8" markerHeight="8" refX="0" refY="4"
            orient="auto">
      <path d="M 8 0 L 0 4 L 8 8 Z" fill="#111"/>
    </marker>
    <marker id="arrow-end" markerWidth="8" markerHeight="8" refX="8" refY="4"
            orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 Z" fill="#111"/>
    </marker>
    <style>
      .dimension {{ fill: none; stroke: #111; stroke-width: 2; marker-start: url(#arrow-start); marker-end: url(#arrow-end); }}
      .box {{ fill: #fff; stroke: #111; stroke-width: 1.5; }}
      .corner {{ fill: #fff; stroke: #111; stroke-width: 1.5; }}
      .dimension-label {{ font: 22px sans-serif; fill: #111; }}
      .coordinate {{ font: 16px sans-serif; fill: #111; }}
      .number {{ font: 56px sans-serif; fill: #111; text-anchor: middle; dominant-baseline: central; }}
      .note {{ font: 18px sans-serif; fill: #333; }}
    </style>
  </defs>
  <rect x="{layout_left}" y="{layout_top}" width="{layout_width:.3f}" height="{layout_height:.3f}" fill="#d0d0d0"/>
  <path class="dimension" d="M {layout_left} 40 H {layout_left + layout_width:.3f}"/>
  <text class="dimension-label" x="{layout_left + layout_width / 2:.3f}" y="30" text-anchor="middle">1.000</text>
  <path class="dimension" d="M {dimension_x:.3f} {layout_top} V {layout_top + layout_height:.3f}"/>
  <text class="dimension-label" x="{dimension_label_x:.3f}" y="{layout_top + layout_height / 2:.3f}" text-anchor="middle">{_number(layout.height_ratio)}</text>
{chr(10).join(elements)}
  <text class="note" x="{layout_left}" y="{note_y:.3f}">Coordinates are normalized independently to layout width and height.</text>
</svg>
'''


def generate_layouts(output_dir: Path = PATH_OUTPUT) -> None:
    """Generate all configured viewset layout diagrams."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for layout in LAYOUTS:
        output = output_dir / f"{layout.name}-normalized-layout.svg"
        output.write_text(render_svg(layout), encoding="utf-8")
        logging.info(f"Generated {output}")


if __name__ == "__main__":
    generate_layouts()
