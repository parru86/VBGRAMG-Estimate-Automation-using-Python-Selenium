"""
parser/estimate_builder.py

Estimate Builder

Responsible for constructing Estimate objects.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from models.estimate import Estimate
from models.specification import Specification
from models.measurement import MeasurementRow


class EstimateBuilder:

    def __init__(self):

        self.reset()

    # -------------------------------------------------

    def reset(self):

        self.estimate = Estimate()

        self.current_specification = None

    # -------------------------------------------------

    def get_estimate(self):

        self.close_specification()

        return self.estimate

    # -------------------------------------------------

    def set_appendix(self, appendix: str):

        self.estimate.appendix_name = appendix.strip()

    # -------------------------------------------------

    def start_specification(
        self,
        code: str,
        description: str,
    ):

        self.close_specification()

        self.current_specification = Specification(

            code=code.strip(),

            description=description.strip(),

            head_description="",

            measurements=[],

            deductions=[],

        )

    # -------------------------------------------------

    def close_specification(self):

        if self.current_specification is None:

            return

        self.estimate.add_specification(

            self.current_specification

        )

        self.current_specification = None

    # -------------------------------------------------

    def set_head_description(self, text: str):

        if self.current_specification is None:

            return

        if self.current_specification.head_description:

            return

        self.current_specification.head_description = text.strip()

    # -------------------------------------------------

    def add_measurement(

        self,

        row: MeasurementRow,

    ):

        if self.current_specification is None:

            return

        self.current_specification.add_measurement(

            row

        )

    # -------------------------------------------------

    def add_deduction(

        self,

        row: MeasurementRow,

    ):

        if self.current_specification is None:

            return

        self.current_specification.add_deduction(

            row

        )

    # -------------------------------------------------

    @property

    def specification(self):

        return self.current_specification
