"""
parser/state_machine.py

Parser State Machine

Responsible for maintaining parser state while reading
VBGRAMG Estimate PDF.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class ParserState(Enum):
    """
    High level parser states.
    """

    START = auto()

    ESTIMATE_HEADER = auto()

    HEADING = auto()

    SPECIFICATION = auto()

    MEASUREMENT_HEADER = auto()

    MEASUREMENT_ROWS = auto()

    DEDUCTION_ROWS = auto()

    MATERIAL_LIST = auto()

    SUMMARY = auto()

    FINISHED = auto()


class ParseMode(Enum):
    """
    Current row parsing mode.
    """

    NONE = auto()

    MEASUREMENT = auto()

    DEDUCTION = auto()


@dataclass(slots=True)
class ParserContext:
    """
    Runtime parser context.

    Stores current position while parsing.
    """

    state: ParserState = ParserState.START

    mode: ParseMode = ParseMode.NONE

    current_heading: str = ""

    current_specification_code: str = ""

    current_specification_description: str = ""

    current_head_description: str = ""

    line_number: int = 0

    specification_index: int = 0

    measurement_count: int = 0

    deduction_count: int = 0

    errors: list[str] = None

    warnings: list[str] = None

    def __post_init__(self):

        if self.errors is None:
            self.errors = []

        if self.warnings is None:
            self.warnings = []

    # --------------------------------------------------

    def next_line(self):

        self.line_number += 1

    # --------------------------------------------------

    def set_heading(
        self,
        heading: str,
    ):

        self.current_heading = heading

    # --------------------------------------------------

    def start_specification(
        self,
        code: str,
        description: str,
    ):

        self.current_specification_code = code

        self.current_specification_description = description

        self.current_head_description = ""

        self.measurement_count = 0

        self.deduction_count = 0

        self.mode = ParseMode.MEASUREMENT

        self.specification_index += 1

        self.state = ParserState.SPECIFICATION

    # --------------------------------------------------

    def start_measurements(self):

        self.mode = ParseMode.MEASUREMENT

        self.state = ParserState.MEASUREMENT_ROWS

    # --------------------------------------------------

    def start_deductions(self):

        self.mode = ParseMode.DEDUCTION

        self.state = ParserState.DEDUCTION_ROWS

    # --------------------------------------------------

    def start_material_list(self):

        self.state = ParserState.MATERIAL_LIST

    # --------------------------------------------------

    def finish_specification(self):

        self.mode = ParseMode.NONE

        self.state = ParserState.HEADING

    # --------------------------------------------------

    def finish(self):

        self.state = ParserState.FINISHED

    # --------------------------------------------------

    def add_measurement(self):

        self.measurement_count += 1

    # --------------------------------------------------

    def add_deduction(self):

        self.deduction_count += 1

    # --------------------------------------------------

    def add_warning(
        self,
        message: str,
    ):

        self.warnings.append(
            f"Line {self.line_number}: {message}"
        )

    # --------------------------------------------------

    def add_error(
        self,
        message: str,
    ):

        self.errors.append(
            f"Line {self.line_number}: {message}"
        )

    # --------------------------------------------------

    @property
    def has_errors(self):

        return len(self.errors) > 0

    # --------------------------------------------------

    @property
    def has_warnings(self):

        return len(self.warnings) > 0

    # --------------------------------------------------

    def __str__(self):

        return (
            "\n"
            "========== PARSER CONTEXT ==========\n"
            f"State              : {self.state.name}\n"
            f"Mode               : {self.mode.name}\n"
            f"Heading            : {self.current_heading}\n"
            f"Specification      : {self.current_specification_code}\n"
            f"Measurements       : {self.measurement_count}\n"
            f"Deductions         : {self.deduction_count}\n"
            f"Line               : {self.line_number}\n"
            "===================================="
        )