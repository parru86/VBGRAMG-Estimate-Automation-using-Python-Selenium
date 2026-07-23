"""
parser/normalizer.py

Text Normalizer

Responsible for cleaning PDF extracted text before parsing.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

import re


class TextNormalizer:

    def normalize(self, text: str) -> list[str]:
        """
        Normalize extracted PDF text.

        Returns:
            Clean list of lines.
        """

        if not text:
            return []

        # Windows → Unix
        text = text.replace("\r", "")

        # Tabs → Space
        text = text.replace("\t", " ")

        # Multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Empty lines remove
        lines = []

        for line in text.split("\n"):

            line = line.strip()

            if not line:
                continue

            lines.append(line)

        return lines

    # --------------------------------------------------

    @staticmethod
    def is_heading(line: str) -> bool:

        return line.startswith("Heading / Description")

    # --------------------------------------------------

    @staticmethod
    def is_specification(line: str) -> bool:

        return bool(
            re.match(
                r"^\d+\s+79\.",
                line,
            )
        )

    # --------------------------------------------------

    @staticmethod
    def is_measurement_header(line: str) -> bool:

        return line.startswith("Sl No Description")

    # --------------------------------------------------

    @staticmethod
    def is_list(line: str) -> bool:

        return line == "LIST"

    # --------------------------------------------------

    @staticmethod
    def is_deduction(line: str) -> bool:

        return line.lower() == "deduction"

    # --------------------------------------------------

    @staticmethod
    def is_total_quantity(line: str) -> bool:

        return line.startswith("Total Quantity")

    # --------------------------------------------------

    @staticmethod
    def is_total_deducted(line: str) -> bool:

        return line.startswith("Total Deducted Quantity")

    # --------------------------------------------------

    @staticmethod
    def is_net_total(line: str) -> bool:

        return line.startswith("Net Total Quantity")