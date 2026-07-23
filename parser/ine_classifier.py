"""
parser/line_classifier.py

VBGRAMG Line Classifier

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

import re
from enum import Enum, auto

from parser.row_parser import RowParser


class LineType(Enum):

    EMPTY = auto()

    HEADING = auto()

    SPECIFICATION = auto()

    HEAD_DESCRIPTION = auto()

    MEASUREMENT_HEADER = auto()

    MEASUREMENT_ROW = auto()

    DEDUCTION = auto()

    LIST = auto()

    MATERIAL_ANALYSIS = auto()

    TOTAL = auto()

    SUMMARY = auto()

    UNKNOWN = auto()


class LineClassifier:

    SPEC_PATTERN = re.compile(
        r"^\d+\s+([0-9A-Za-z]+\.[0-9A-Za-z\.]+)\s+--"
    )

    def __init__(self):

        self.row_parser = RowParser()

    # ---------------------------------------------------------

    def classify(
        self,
        line: str,
    ) -> LineType:

        if line is None:

            return LineType.EMPTY

        line = " ".join(line.split())

        if line == "":

            return LineType.EMPTY

        lower = line.lower()

        # -----------------------------------------------------
        # Heading
        # -----------------------------------------------------

        if "heading / description" in lower:

            return LineType.HEADING

        # -----------------------------------------------------
        # Specification
        # -----------------------------------------------------

        if self.SPEC_PATTERN.match(line):

            return LineType.SPECIFICATION

        # -----------------------------------------------------
        # Measurement Header
        # -----------------------------------------------------

        if (
            "sl no" in lower
            and "description" in lower
            and "length" in lower
        ):

            return LineType.MEASUREMENT_HEADER

        # -----------------------------------------------------
        # Deduction
        # -----------------------------------------------------

        if lower == "deduction":

            return LineType.DEDUCTION

        # -----------------------------------------------------
        # LIST
        # -----------------------------------------------------

        if lower == "list":

            return LineType.LIST

        # -----------------------------------------------------
        # Material Analysis
        # -----------------------------------------------------

        if "material analysis" in lower:

            return LineType.MATERIAL_ANALYSIS

        # -----------------------------------------------------
        # Totals
        # -----------------------------------------------------

        if (
            "total quantity" in lower
            or "net quantity" in lower
        ):

            return LineType.TOTAL

        # -----------------------------------------------------
        # Summary
        # -----------------------------------------------------

        summary_keywords = (

            "labour cost",

            "material cost",

            "carriage cost",

            "rate per unit",

            "say",

            "add",

            "total cost",

        )

        if any(k in lower for k in summary_keywords):

            return LineType.SUMMARY

        # -----------------------------------------------------
        # Measurement Row
        # -----------------------------------------------------

        if self.row_parser.parse(line) is not None:

            return LineType.MEASUREMENT_ROW

        # -----------------------------------------------------
        # Head Description
        # -----------------------------------------------------

        if self.is_head_description(line):

            return LineType.HEAD_DESCRIPTION

        # -----------------------------------------------------

        return LineType.UNKNOWN

    # =========================================================

    def is_head_description(
        self,
        line: str,
    ) -> bool:

        lower = line.lower()

        blocked = (

            "heading",

            "description",

            "deduction",

            "list",

            "material analysis",

            "total quantity",

            "net quantity",

            "labour cost",

            "material cost",

            "carriage",

            "sl no",

        )

        if any(word in lower for word in blocked):

            return False

        if self.SPEC_PATTERN.match(line):

            return False

        if self.row_parser.parse(line) is not None:

            return False

        return True