"""
parser/row_buffer.py

VBGRAMG Row Buffer

Combines wrapped PDF lines into complete
measurement/deduction rows before parsing.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

import re


class RowBuffer:
    """
    Buffers wrapped PDF lines.

    Example

    COLUMN
    PLINTH TO
    SLAB
    30 0.200 3.000 1.0 18.000

    becomes

    COLUMN PLINTH TO SLAB 30 0.200 3.000 1.0 18.000
    """

    ROW_START = re.compile(r"^\d+\s+")

    def __init__(self):

        self._buffer: list[str] = []

    # ---------------------------------------------------------

    def clear(self):

        self._buffer.clear()

    # ---------------------------------------------------------

    def has_data(self) -> bool:

        return len(self._buffer) > 0

    # ---------------------------------------------------------

    def push(
        self,
        line: str,
    ):

        line = " ".join(line.split())

        if line:

            self._buffer.append(line)

    # ---------------------------------------------------------

    def text(self) -> str:

        return " ".join(self._buffer).strip()

    # ---------------------------------------------------------

    def pop(self) -> str:

        value = self.text()

        self.clear()

        return value

    # ---------------------------------------------------------

    @classmethod
    def is_row_start(
        cls,
        line: str,
    ) -> bool:

        return bool(cls.ROW_START.match(line.strip()))

    # ---------------------------------------------------------

    @classmethod
    def should_continue(
        cls,
        line: str,
    ) -> bool:
        """
        Returns True if this line is a continuation
        of the previous row.
        """

        line = line.strip()

        if not line:

            return False

        keywords = (
            "LIST",
            "Heading / Description",
            "deduction",
            "Material Analysis",
            "Total Quantity",
            "Net Total Quantity",
            "Total Deducted Quantity",
            "Say",
            "Unskilled wage",
            "Unskilled Person-days",
            "Code Description",
            "Sl No",
        )

        for keyword in keywords:

            if line.startswith(keyword):

                return False

        return not cls.is_row_start(line)