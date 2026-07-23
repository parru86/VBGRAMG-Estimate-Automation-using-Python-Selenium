"""
=========================================================
VBGRAMG AUTO ESTIMATE

MEASUREMENT PARSER TEST

=========================================================
"""

from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector
from parser.measurement_parser import MeasurementParser


def main():

    print("=" * 80)
    print("MEASUREMENT PARSER TEST")
    print("=" * 80)

    # --------------------------------------------------

    engine = PDFEngine("pdf/model.pdf")

    pages = engine.open()

    rows = RowDetector().detect_all(pages)

    blocks = ItemDetector().detect(rows)

    parser = MeasurementParser()

    # --------------------------------------------------

    for block in blocks:

        print()
        print("=" * 80)

        print(f"ITEM : {block.item_no}")

        print(f"CODE : {block.item_code}")

        print(f"DESCRIPTION : {block.description}")

        print("=" * 80)

        measurements = parser.parse(block)

        print(f"TOTAL MEASUREMENTS : {len(measurements)}")

        print()

        for m in measurements:

            print("-" * 50)

            print(f"SL          : {m.sl}")

            print(f"Description : {m.description}")

            print(f"No          : {m.no}")

            print(f"Length      : {m.length}")

            print(f"Breadth     : {m.breadth}")

            print(f"Depth       : {m.depth}")

            print(f"CF          : {m.cf}")

            print(f"Quantity    : {m.quantity}")

            print(f"Volume      : {m.volume}")

        print()


if __name__ == "__main__":

    main()