from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.item_detector import ItemDetector


def main():

    print("=" * 70)
    print("MEASUREMENT ROW DIAGNOSTIC")
    print("=" * 70)

    # ---------------------------------------

    engine = PDFEngine("pdf/model.pdf")

    pages = engine.open()

    rows = RowDetector().detect_all(pages)

    blocks = ItemDetector().detect(rows)

    # ---------------------------------------

    block = blocks[0]

    print()

    print("ITEM :", block.item_no)

    print("CODE :", block.item_code)

    print()

    print("Measurement Rows :", block.measurement_count)

    print()

    # ---------------------------------------

    for index, row in enumerate(block.measurement_rows):

        print("=" * 70)

        print("Measurement Row", index + 1)

        print()

        print("TEXT")

        print(row.text)

        print()

        print("WORDS")

        print("-" * 70)

        for i, word in enumerate(row.words):

            print(
                f"{i:02d} : '{word.text}'"
            )

        print()


if __name__ == "__main__":
    main()