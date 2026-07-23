"""
parser/row_parser.py

VBGRAMG Row Parser

Parses one Measurement/Deduction row.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

import re

from models.measurement import MeasurementRow


class RowParser:
    """
    Parses Measurement/Deduction rows.
    """

    ROW_PATTERN = re.compile(
        r"""
        ^\s*
        (\d+)                     # Sl No
        \s+
        (.+?)                     # Description
        \s+
        (\S+)                     # No
        \s+
        (\S+)                     # Length
        (?:\s+(\S+))?             # Breadth
        (?:\s+(\S+))?             # Depth
        (?:\s+(\S+))?             # CF
        (?:\s+(.*))?              # Remark
        $
        """,
        re.VERBOSE,
    )

    # ---------------------------------------------------------

    def is_row(self, line: str) -> bool:
        """
        Returns True if line looks like a measurement row.
        """

        line = line.strip()

        if not line:
            return False

        if not line[0].isdigit():
            return False

        return True

    # ---------------------------------------------------------

    def parse(self, line: str) -> MeasurementRow | None:
        """
        Parse one measurement row.
        """

        line = " ".join(line.split())

        match = self.ROW_PATTERN.match(line)

        if match is None:
            return None

        (
            _,
            description,
            no,
            length,
            breadth,
            depth,
            cf,
            remark,
        ) = match.groups()

        return MeasurementRow(

            item_description=description.strip(),

            no=no or "",

            length=length or "",

            breadth=breadth or "",

            depth=depth or "",

            cf=cf or "1",

            remark=(remark or "").strip(),
        )

    # ---------------------------------------------------------

    def parse_rows(
        self,
        lines: list[str],
    ) -> list[MeasurementRow]:

        rows = []

        for line in lines:

            row = self.parse(line)

            if row:

                rows.append(row)

        return rows