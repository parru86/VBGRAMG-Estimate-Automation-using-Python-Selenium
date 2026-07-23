"""
=========================================================
VBGRAMG AUTO ESTIMATE
VALIDATOR TEST
=========================================================
"""

from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector
from parser.estimate_parser import EstimateParser
from parser.validator import Validator


def main():

    print("=" * 80)
    print("VALIDATOR TEST")
    print("=" * 80)

    # --------------------------------------------------

    engine = PDFEngine("pdf/model.pdf")

    pages = engine.open()

    rows = RowDetector().detect_all(pages)

    blocks = ItemDetector().detect(rows)

    estimate = EstimateParser().parse(blocks)

    # --------------------------------------------------

    validator = Validator()

    result = validator.validate(estimate)

    # --------------------------------------------------

    print()

    print(f"Passed        : {result.passed}")

    print(f"Errors        : {result.error_count}")

    print(f"Warnings      : {result.warning_count}")

    print()

    # --------------------------------------------------

    if result.errors:

        print("=" * 80)

        print("ERRORS")

        print("=" * 80)

        for error in result.errors:

            print(error)

        print()

    # --------------------------------------------------

    if result.warnings:

        print("=" * 80)

        print("WARNINGS")

        print("=" * 80)

        for warning in result.warnings:

            print(warning)

        print()

    print("=" * 80)

    print("VALIDATION COMPLETE")

    print("=" * 80)


if __name__ == "__main__":

    main()