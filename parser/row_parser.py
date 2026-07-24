"""
parser/row_parser.py

VBGRAMG Row Parser

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

import re

from models.measurement import MeasurementRow


class RowParser:
    """
    Parse a single Measurement / Deduction row.

    Supports

    ✔ Formula in Length
    ✔ Negative Quantity
    ✔ Dot (.) Description
    ✔ Empty Breadth
    ✔ Empty Depth
    ✔ Empty Remark
    """

    NUMBER = r"-?[0-9.]+"

    ROW_PATTERN = re.compile(
        rf"""
        ^\s*
        (?P<sl>\d+)
        \s+

        (?P<desc>.+?)

        \s+

        (?P<no>\S+)

        \s+

        (?P<length>\S+)

        (?:\s+(?P<breadth>\S+))?

        (?:\s+(?P<depth>\S+))?

        (?:\s+(?P<cf>{NUMBER}))?

        (?:\s+(?P<qty>{NUMBER}))?

        (?:\s+(?P<remark>.*))?

        $
        """,
        re.VERBOSE,
    )

    # -----------------------------------------------------

    def parse(
        self,
        line: str,
    ) -> MeasurementRow | None:

        if line is None:
            return None

        line = " ".join(line.split())

        if line == "":
            return None

        match = self.ROW_PATTERN.match(line)

        if match is None:
            return None

        groups = match.groupdict()

        description = groups["desc"].strip()

        if description == ".":

            description = "."

        return MeasurementRow(

            item_description=description,

            no=(groups["no"] or "").strip(),

            length=(groups["length"] or "").strip(),

            breadth=(groups["breadth"] or "").strip(),

            depth=(groups["depth"] or "").strip(),

            cf=(groups["cf"] or "1").strip(),

            remark=(groups["remark"] or "").strip(),

        )

    # -----------------------------------------------------

    def is_row(
        self,
        line: str,
    ) -> bool:

        return self.parse(line) is not None

    # -----------------------------------------------------

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