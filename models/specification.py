"""
models/specification.py

Specification Model

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from dataclasses import dataclass, field

from models.measurement import MeasurementRow


@dataclass(slots=True)
class Specification:
    """
    Represents one Specification.
    """

    code: str

    description: str

    head_description: str = ""

    measurements: list[MeasurementRow] = field(default_factory=list)

    deductions: list[MeasurementRow] = field(default_factory=list)

    def add_measurement(
        self,
        row: MeasurementRow,
    ) -> None:

        if not row.is_empty:
            self.measurements.append(row)

    def add_deduction(
        self,
        row: MeasurementRow,
    ) -> None:

        if not row.is_empty:
            self.deductions.append(row)

    @property
    def has_deduction(self) -> bool:

        return len(self.deductions) > 0

    def __str__(self):

        return (
            f"{self.code} | "
            f"Measurements={len(self.measurements)} | "
            f"Deductions={len(self.deductions)}"
        )