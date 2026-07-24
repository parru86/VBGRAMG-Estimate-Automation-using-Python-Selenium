"""
tests/test_parser.py

Parser Test

Run:

py tests/test_parser.py
"""

from pathlib import Path

from parser.estimate_parser import EstimateParser


def main():

    pdf = Path("sample_pdfs/Food_Building.pdf")

    parser = EstimateParser()

    estimate = parser.parse(pdf)

    print("=" * 60)

    print(estimate)

    print("=" * 60)

    print("Specifications :", estimate.total_specifications)

    print("Measurements  :", estimate.total_measurements)

    print("Deductions    :", estimate.total_deductions)

    print("=" * 60)


if __name__ == "__main__":

    main()