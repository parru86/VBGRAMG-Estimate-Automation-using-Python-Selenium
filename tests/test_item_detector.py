from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector


def main():

    pdf_file = "pdf/model.pdf"

    print("=" * 60)
    print("VBGRAMG ITEM DETECTOR TEST")
    print("=" * 60)

    # -----------------------------------------
    # PDF
    # -----------------------------------------

    engine = PDFEngine(pdf_file)

    pages = engine.open()

    print(f"Pages : {len(pages)}")

    # -----------------------------------------
    # ROWS
    # -----------------------------------------

    detector = RowDetector()

    rows = detector.detect_all(pages)

    print(f"Rows : {len(rows)}")

    # -----------------------------------------
    # ITEMS
    # -----------------------------------------

    item_detector = ItemDetector()

    blocks = item_detector.detect(rows)

    print(f"\nTOTAL ITEMS : {len(blocks)}")

    # -----------------------------------------

    for block in blocks:

        print("-" * 60)

        print(f"Item No      : {block.item_no}")

        print(f"Item Code    : {block.item_code}")

        print(f"Description  : {block.description}")

        print(f"Rows         : {block.row_count}")

        print(f"Measurements : {block.measurement_count}")

        print(f"Rate Rows    : {block.rate_count}")

        print(f"Pages        : {block.start_page} -> {block.end_page}")

    print("\nDONE")


if __name__ == "__main__":
    main()