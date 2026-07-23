"""
=========================================================
VBGRAMG AUTO ESTIMATE
MEASUREMENT PATTERN ANALYZER
=========================================================

Purpose

Analyze all sample PDFs and print every
measurement row found in the estimate.

This script is for development only.

=========================================================
"""

from pathlib import Path

from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector


# ---------------------------------------------------------


def analyze_pdf(pdf_file: Path):

    print()
    print("=" * 100)
    print(f"FILE : {pdf_file.name}")
    print("=" * 100)

    engine = PDFEngine(str(pdf_file))

    pages = engine.open()

    rows = RowDetector().detect_all(pages)

    blocks = ItemDetector().detect(rows)

    print(
        f"Pages : {len(pages)}    "
        f"Rows : {len(rows)}    "
        f"Items : {len(blocks)}"
    )

    print()

    for block in blocks:

        print("-" * 100)

        print(
            f"ITEM {block.item_no}    "
            f"CODE : {block.item_code}"
        )

        print(
            f"Measurement Rows : "
            f"{block.measurement_count}"
        )

        print()

        for row in block.measurement_rows:

            print(row.text)

        print()


# ---------------------------------------------------------


def main():

    sample_folder = Path("pdf/samples")

    if not sample_folder.exists():

        print("Sample folder not found.")

        return

    pdf_files = sorted(sample_folder.glob("*.pdf"))

    if not pdf_files:

        print("No PDF files found.")

        return

    print()
    print("=" * 100)
    print("VBGRAMG MEASUREMENT PATTERN ANALYZER")
    print("=" * 100)

    for pdf in pdf_files:

        analyze_pdf(pdf)


# ---------------------------------------------------------

if __name__ == "__main__":

    main()