"""
parser/pdf_reader.py

PDF Reader

Reads VBGRAMG Estimate PDF using PyMuPDF.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from pathlib import Path

import fitz


class PDFReader:
    """
    Reads PDF and returns page text.
    """

    def __init__(self):

        self.document = None

    # --------------------------------------------------

    def open(
        self,
        pdf_file: str | Path,
    ) -> None:

        pdf_file = Path(pdf_file)

        if not pdf_file.exists():

            raise FileNotFoundError(pdf_file)

        self.document = fitz.open(pdf_file)

    # --------------------------------------------------

    def close(self):

        if self.document:

            self.document.close()

            self.document = None

    # --------------------------------------------------

    @property
    def page_count(self) -> int:

        if self.document is None:

            return 0

        return len(self.document)

    # --------------------------------------------------

    def page_text(
        self,
        page_number: int,
    ) -> str:

        if self.document is None:

            raise RuntimeError(
                "PDF is not opened."
            )

        page = self.document.load_page(
            page_number
        )

        return page.get_text()

    # --------------------------------------------------

    def pages(self):

        if self.document is None:

            raise RuntimeError(
                "PDF is not opened."
            )

        for page_number in range(
            len(self.document)
        ):

            yield (
                page_number + 1,
                self.page_text(page_number),
            )

    # --------------------------------------------------

    def read(
        self,
        pdf_file: str | Path,
    ) -> str:

        self.open(pdf_file)

        text = []

        for _, page_text in self.pages():

            text.append(page_text)

        self.close()

        return "\n".join(text)

    # --------------------------------------------------

    def read_pages(
        self,
        pdf_file: str | Path,
    ) -> list[str]:

        self.open(pdf_file)

        pages = []

        for _, page_text in self.pages():

            pages.append(page_text)

        self.close()

        return pages