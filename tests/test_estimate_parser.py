"""
=========================================================
VBGRAMG AUTO ESTIMATE

ESTIMATE PARSER TEST

=========================================================
"""

from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector
from parser.estimate_parser import EstimateParser


def main():

    print("=" * 80)
    print("ESTIMATE PARSER TEST")
    print("=" * 80)

    # --------------------------------------------------

    engine = PDFEngine("pdf/model.pdf")

    pages = engine.open()

    rows = RowDetector().detect_all(pages)

    blocks = ItemDetector().detect(rows)

    estimate = EstimateParser().parse(blocks)

    # --------------------------------------------------

    print()

    print("SUMMARY")

    print("-" * 80)

    print(f"Total Items         : {estimate.item_count}")

    print(f"Total Measurements  : {estimate.measurement_count}")

    print(f"Total Quantity      : {estimate.total_quantity}")

    print()

    # --------------------------------------------------

    for item in estimate.items:

        print("=" * 80)

        print(f"ITEM : {item.item_no}")

        print(f"CODE : {item.item_code}")

        print(f"DESCRIPTION :")

        print(item.description)

        print()

        print(f"Measurements : {item.measurement_count}")

        print(f"Quantity     : {item.total_quantity}")

        print(f"Volume       : {item.total_volume}")

        print()

        for m in item.measurements:

            print(

                f"SL={m.sl:<3}"

                f" Qty={m.quantity:<10}"

                f" Desc={m.description}"

            )

        print()

    print("=" * 80)

    print("DONE")


if __name__ == "__main__":

    main()