"""
=========================================================
VBGRAMG AUTO ESTIMATE
PDF ENGINE
=========================================================
"""

from pathlib import Path
import pdfplumber

from models.word import Word


class PDFEngine:

    """
    Read PDF and return Word Objects.
    """

    def __init__(self, pdf_path: str):

        self.pdf_path = Path(pdf_path)

        self.pages = []

    # -----------------------------------------------------

    def exists(self):

        return self.pdf_path.exists()

    # -----------------------------------------------------

    def open(self):

        if not self.exists():

            raise FileNotFoundError(

                f"{self.pdf_path} not found."

            )

        self.pages.clear()

        with pdfplumber.open(self.pdf_path) as pdf:

            for page_no, page in enumerate(pdf.pages, start=1):

                words = []

                extracted = page.extract_words(

                    keep_blank_chars=False,

                    use_text_flow=True,

                    x_tolerance=2,

                    y_tolerance=2

                )

                for w in extracted:

                    words.append(

                        Word(

                            page=page_no,

                            text=w["text"],

                            x0=round(w["x0"], 2),

                            x1=round(w["x1"], 2),

                            top=round(w["top"], 2),

                            bottom=round(w["bottom"], 2)

                        )

                    )

                self.pages.append(words)

        return self.pages

    # -----------------------------------------------------

    @property
    def page_count(self):

        return len(self.pages)

    # -----------------------------------------------------

    def page(self, number):

        return self.pages[number - 1]

    # -----------------------------------------------------

    def info(self):

        return {

            "file": str(self.pdf_path),

            "pages": self.page_count

        }