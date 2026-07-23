"""
models/estimate.py

Estimate Model

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from dataclasses import dataclass, field

from models.specification import Specification


@dataclass(slots=True)
class Estimate:
    """
    Complete Estimate.
    """

    work_name: str = ""

    work_code: str = ""

    scheme: str = ""

    block: str = ""

    gram_panchayat: str = ""

    appendix_name: str = ""

    specifications: list[Specification] = field(
        default_factory=list
    )

    def add_specification(
        self,
        specification: Specification,
    ) -> None:

        self.specifications.append(specification)

    @property
    def total_specifications(self) -> int:

        return len(self.specifications)

    @property
    def total_measurements(self) -> int:

        return sum(
            len(s.measurements)
            for s in self.specifications
        )

    @property
    def total_deductions(self) -> int:

        return sum(
            len(s.deductions)
            for s in self.specifications
        )

    def __str__(self):

        return (
            f"{self.work_name}\n"
            f"Specifications : {self.total_specifications}\n"
            f"Measurements : {self.total_measurements}\n"
            f"Deductions : {self.total_deductions}"
        )