"""
models/measurement.py

Measurement Row Model

Used for:
    • Measurement Rows
    • Deduction Rows

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MeasurementRow:
    """
    Represents one Measurement/Deduction row.
    """

    item_description: str = ""

    no: str = ""

    length: str = ""

    breadth: str = ""

    depth: str = ""

    cf: str = "1"

    remark: str = ""

    @property
    def is_empty(self) -> bool:

        return (
            self.item_description.strip() == ""
            and self.no.strip() == ""
            and self.length.strip() == ""
            and self.breadth.strip() == ""
            and self.depth.strip() == ""
        )

    def __str__(self) -> str:

        return (
            f"{self.item_description} | "
            f"N={self.no} "
            f"L={self.length} "
            f"B={self.breadth} "
            f"D={self.depth} "
            f"CF={self.cf}"
        )