"""Tests for generated viewset layout diagrams."""

import tempfile
import unittest
from decimal import Decimal
from pathlib import Path
from xml.etree import ElementTree

from dent_oip_builder.viewset_layout_maker import LAYOUTS, calculate_boxes, generate_layouts


class TestViewsetLayoutMaker(unittest.TestCase):
    def test_all_layout_geometry(self):
        expected_counts = {"VS-01": 9, "VS-02": 13, "VS-03": 13, "VS-04": 12}
        precision = Decimal("0.001")

        self.assertEqual(set(expected_counts), {layout.name for layout in LAYOUTS})
        for layout in LAYOUTS:
            boxes = calculate_boxes(layout)
            self.assertEqual(expected_counts[layout.name], len(boxes))
            for row in layout.rows:
                row_boxes = boxes[row.first_number - 1 : row.first_number - 1 + row.box_count]
                self.assertEqual(row.box_count, len(row_boxes))
                self.assertEqual(
                    {layout.geometry.box_aspect_ratios[row.row_type]},
                    {
                        (box.width / box.height).quantize(precision)
                        for box in row_boxes
                    },
                )

    def test_vs04_geometry(self):
        vs04 = next(layout for layout in LAYOUTS if layout.name == "VS-04")
        boxes = calculate_boxes(vs04)

        expected_coordinates = {
            1: ("0.034", "0.607", "0.254", "0.954"),
            5: ("0.034", "0.236", "0.254", "0.584"),
            9: ("0.034", "0.046", "0.254", "0.214"),
            12: ("0.746", "0.046", "0.966", "0.214"),
        }
        for number, expected in expected_coordinates.items():
            box = boxes[number - 1]
            actual = (
                f"{box.left / vs04.width:.3f}",
                f"{box.bottom / vs04.height:.3f}",
                f"{(box.left + box.width) / vs04.width:.3f}",
                f"{(box.bottom + box.height) / vs04.height:.3f}",
            )
            self.assertEqual(expected, actual)

    def test_vs02_inherits_vs01_geometry(self):
        vs01 = next(layout for layout in LAYOUTS if layout.name == "VS-01")
        vs02 = next(layout for layout in LAYOUTS if layout.name == "VS-02")

        self.assertEqual(
            tuple(row.row_type for row in vs01.rows),
            tuple(row.row_type for row in vs02.rows),
        )
        self.assertEqual(vs01.geometry, vs02.geometry)
        self.assertEqual(vs01.box_width, vs02.box_width)
        self.assertEqual(vs01.height, vs02.height)
        self.assertEqual(Decimal("0.429"), vs02.height_ratio.quantize(Decimal("0.001")))

        boxes = calculate_boxes(vs02)
        expected_coordinates = {
            1: ("0.023", "0.544", "0.172", "0.947"),
            7: ("0.184", "0.274", "0.333", "0.518"),
            11: ("0.264", "0.053", "0.414", "0.247"),
            13: ("0.586", "0.053", "0.736", "0.247"),
        }
        for number, expected in expected_coordinates.items():
            box = boxes[number - 1]
            actual = (
                f"{box.left / vs02.width:.3f}",
                f"{box.bottom / vs02.height:.3f}",
                f"{(box.left + box.width) / vs02.width:.3f}",
                f"{(box.bottom + box.height) / vs02.height:.3f}",
            )
            self.assertEqual(expected, actual)

    def test_generates_valid_svg(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            generate_layouts(output_dir)
            for layout in LAYOUTS:
                output = output_dir / f"{layout.name}-normalized-layout.svg"
                self.assertTrue(output.exists())
                root = ElementTree.parse(output).getroot()
                namespace = {"svg": "http://www.w3.org/2000/svg"}
                box_count = sum(row.box_count for row in layout.rows)
                self.assertEqual(
                    2 * box_count,
                    len(root.findall(".//svg:circle", namespace)),
                )
                vertical_label = next(
                    element
                    for element in root.findall(".//svg:text", namespace)
                    if element.text == f"{layout.height_ratio:.3f}"
                )
                self.assertGreaterEqual(
                    Decimal(root.attrib["width"]) - Decimal(vertical_label.attrib["x"]),
                    Decimal(75),
                )


if __name__ == "__main__":
    unittest.main()
