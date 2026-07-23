"""
=========================================================
VBGRAMG AUTO ESTIMATE
TEST ALL SAMPLE PDFs
=========================================================
"""

from pathlib import Path

from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector


# ---------------------------------------------------------


def test_pdf(pdf_path: Path):

    try:

        # PDF

        engine = PDFEngine(str(pdf_path))

        pages = engine.open()

        # Rows

        row_detector = RowDetector()

        rows = row_detector.detect_all(pages)

        # Items

        item_detector = ItemDetector()

        blocks = item_detector.detect(rows)

        return {

            "file": pdf_path.name,

            "pages": len(pages),

            "rows": len(rows),

            "items": len(blocks),

            "status": "PASS"

        }

    except Exception as e:

        return {

            "file": pdf_path.name,

            "pages": "-",

            "rows": "-",

            "items": "-",

            "status": f"FAIL ({e})"

        }


# ---------------------------------------------------------


def main():

    sample_folder = Path("pdf/samples")

    if not sample_folder.exists():

        print("Sample Folder Not Found")

        return

    pdf_files = sorted(

        sample_folder.glob("*.pdf")

    )

    if not pdf_files:

        print("No PDF Found")

        return

    print("=" * 90)

    print("VBGRAMG SAMPLE VALIDATION")

    print("=" * 90)

    print(

        f"{'FILE':25}"

        f"{'PAGES':>8}"

        f"{'ROWS':>10}"

        f"{'ITEMS':>10}"

        f"{'STATUS':>15}"

    )

    print("-" * 90)

    passed = 0

    failed = 0

    for pdf in pdf_files:

        result = test_pdf(pdf)

        print(

            f"{result['file'][:25]:25}"

            f"{str(result['pages']):>8}"

            f"{str(result['rows']):>10}"

            f"{str(result['items']):>10}"

            f"{result['status']:>15}"

        )

        if result["status"] == "PASS":

            passed += 1

        else:

            failed += 1

    print("=" * 90)

    print(f"TOTAL FILES : {len(pdf_files)}")

    print(f"PASSED      : {passed}")

    print(f"FAILED      : {failed}")

    print("=" * 90)


# ---------------------------------------------------------

if __name__ == "__main__":

    main()