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
class RowDefinition:
    """A top-to-bottom row in a viewset layout."""

    box_count: int
    first_number: int
    box_aspect_ratio: Decimal
    row_type: str


@dataclass(frozen=True)
class LayoutDefinition:
    """Physical proportions used to calculate normalized box coordinates."""

    name: str
    expected_height_ratio: Decimal
    rows: tuple[RowDefinition, ...]
    horizontal_margin: Decimal
    vertical_margin: Decimal
    horizontal_gap: Decimal
    vertical_gap: Decimal

    @property
    def box_width(self) -> Decimal:
        """Return the common box width relative to a layout width of one."""
        max_columns = max(row.box_count for row in self.rows)
        return (
            Decimal(1)
            - 2 * self.horizontal_margin
            - (max_columns - 1) * self.horizontal_gap
        ) / max_columns

    @property
    def height_ratio(self) -> Decimal:
        """Calculate layout height from margins, gaps, and row proportions."""
        row_heights = sum(
            self.box_width / row.box_aspect_ratio for row in self.rows
        )
        return (
            2 * self.vertical_margin
            + (len(self.rows) - 1) * self.vertical_gap
            + row_heights
        )


@dataclass(frozen=True)
class Box:
    """A box in physical units relative to a layout width of one."""

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


def load_layout(path: Path) -> LayoutDefinition:
    """Load one normative viewset layout table."""
    with path.open(encoding="utf-8", newline="") as input_file:
        records = list(csv.DictReader(input_file))
    if not records:
        raise ValueError(f"No rows defined in {path}")

    first = records[0]
    repeated_fields = (
        "Layout Width",
        "Layout Height",
        "Horizontal Margin",
        "Vertical Margin",
        "Horizontal Gap",
        "Vertical Gap",
    )
    for record in records[1:]:
        for field in repeated_fields:
            if record[field] != first[field]:
                raise ValueError(f"Inconsistent {field} in {path}")
    if _decimal(first["Layout Width"]) != 1:
        raise ValueError(f"Layout Width must be 1.000 in {path}")

    rows = tuple(
        RowDefinition(
            box_count=int(record["Boxes"]),
            first_number=int(record["First ILC"]),
            box_aspect_ratio=_decimal(record["Box Width:Height"]),
            row_type=record["Row Type"],
        )
        for record in records
    )
    layout = LayoutDefinition(
        name=path.stem,
        expected_height_ratio=_decimal(first["Layout Height"]),
        rows=rows,
        horizontal_margin=_decimal(first["Horizontal Margin"]),
        vertical_margin=_decimal(first["Vertical Margin"]),
        horizontal_gap=_decimal(first["Horizontal Gap"]),
        vertical_gap=_decimal(first["Vertical Gap"]),
    )
    if layout.height_ratio.quantize(Decimal("0.001")) != layout.expected_height_ratio:
        raise ValueError(f"Calculated Layout Height does not match {path}")
    return layout


LAYOUTS = tuple(load_layout(path) for path in sorted(PATH_LAYOUTS.glob("VS-*.csv")))


def calculate_boxes(layout: LayoutDefinition) -> tuple[Box, ...]:
    """Calculate boxes from row proportions, without hand-entered coordinates."""
    box_width = layout.box_width
    row_heights = tuple(box_width / row.box_aspect_ratio for row in layout.rows)

    boxes = []
    bottom = layout.vertical_margin
    for row, row_height in reversed(tuple(zip(layout.rows, row_heights))):
        row_width = row.box_count * box_width + (row.box_count - 1) * layout.horizontal_gap
        left = (Decimal(1) - row_width) / 2
        for index in range(row.box_count):
            boxes.append(
                Box(
                    number=row.first_number + index,
                    left=left + index * (box_width + layout.horizontal_gap),
                    bottom=bottom,
                    width=box_width,
                    height=row_height,
                )
            )
        bottom += row_height + layout.vertical_gap

    return tuple(sorted(boxes, key=lambda box: box.number))


def _number(value: Decimal) -> str:
    return f"{value:.3f}"


def render_svg(layout: LayoutDefinition) -> str:
    """Render a self-contained SVG with dimensions and normalized coordinates."""
    page_width = Decimal(1200)
    layout_left = Decimal(80)
    layout_top = Decimal(100)
    scale = Decimal(1000)
    layout_width = scale
    layout_height = layout.height_ratio * scale
    page_height = layout_top + layout_height + Decimal(100)
    note_y = layout_top + layout_height + Decimal(60)
    boxes = calculate_boxes(layout)

    elements = []
    for box in boxes:
        x = layout_left + box.left * scale
        y = layout_top + layout_height - (box.bottom + box.height) * scale
        width = box.width * scale
        height = box.height * scale
        left = box.left
        right = box.left + box.width
        bottom = box.bottom / layout.height_ratio
        top = (box.bottom + box.height) / layout.height_ratio
        elements.append(
            f'''  <g>
    <rect class="box" x="{x:.3f}" y="{y:.3f}" width="{width:.3f}" height="{height:.3f}"/>
    <circle class="corner" cx="{x:.3f}" cy="{y:.3f}" r="7"/>
    <circle class="corner" cx="{x + width:.3f}" cy="{y + height:.3f}" r="7"/>
    <text class="coordinate" x="{x + 10:.3f}" y="{y + 24:.3f}">({_number(left)}, {_number(top)})</text>
    <text class="coordinate" x="{x + width - 10:.3f}" y="{y + height - 10:.3f}" text-anchor="end">({_number(right)}, {_number(bottom)})</text>
    <text class="number" x="{x + width / 2:.3f}" y="{y + height / 2:.3f}">{box.number}</text>
  </g>'''
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{page_width}" height="{page_height}"
     viewBox="0 0 {page_width} {page_height}" role="img"
     aria-labelledby="title description">
  <title id="title">{layout.name} normalized layout</title>
  <desc id="description">
    Boxes calculated from normative row proportions. Coordinates are normalized
    independently to layout width and height. The physical layout has a
    width-to-height ratio of 1.000 to {layout.height_ratio}.
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
  <rect x="{layout_left}" y="{layout_top}" width="{layout_width}" height="{layout_height}" fill="#d0d0d0"/>
  <path class="dimension" d="M {layout_left} 58 H {layout_left + layout_width}"/>
  <text class="dimension-label" x="{layout_left + layout_width / 2}" y="48" text-anchor="middle">1.000</text>
  <path class="dimension" d="M 1125 {layout_top} V {layout_top + layout_height}"/>
  <text class="dimension-label" x="1142" y="{layout_top + layout_height / 2}">{layout.height_ratio}</text>
{chr(10).join(elements)}
  <text class="note" x="80" y="{note_y}">Coordinates are normalized independently to layout width and height.</text>
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
