"""
parser/estimate_parser.py

VBGRAMG Estimate Parser

Project:
VBGRAMG Estimate Automation

Author:
Parmeshwar Verma

Workflow

PDF
 ↓
PDFReader
 ↓
Normalizer
 ↓
LineClassifier
 ↓
EstimateBuilder
 ↓
Estimate
"""

from __future__ import annotations

from pathlib import Path

from models.estimate import Estimate

from parser.pdf_reader import PDFReader
from parser.normalizer import TextNormalizer
from parser.line_classifier import (
    LineClassifier,
    LineType,
)
from parser.row_parser import RowParser
from parser.estimate_builder import EstimateBuilder
from parser.state_machine import (
    ParserContext,
    ParserState,
    ParseMode,
)


class EstimateParser:

    def __init__(self):

        self.reader = PDFReader()

        self.normalizer = TextNormalizer()

        self.classifier = LineClassifier()

        self.row_parser = RowParser()

        self.builder = EstimateBuilder()

        self.context = ParserContext()

        self.lines: list[str] = []

        self.index = 0

    # ==========================================================
    # PUBLIC API
    # ==========================================================

    def parse(
        self,
        pdf_path: str | Path,
    ) -> Estimate:

        self.reset()

        raw_text = self.reader.read(pdf_path)

        self.lines = self.normalizer.normalize(
            raw_text
        )

        self.parse_lines()

        self.validate()

        return self.finish()

    # ==========================================================

    def reset(self):

        self.builder.reset()

        self.context = ParserContext()

        self.lines = []

        self.index = 0

    # ==========================================================

    def parse_lines(self):

        while not self.eof():

            line_type = self.classify_current_line()

            self.dispatch(line_type)

            self.advance()

    # ==========================================================

    def classify_current_line(
        self,
    ) -> LineType:

        return self.classifier.classify(
            self.current_line
        )

    # ==========================================================

    def dispatch(
        self,
        line_type: LineType,
    ):

        if line_type == LineType.EMPTY:
            return

        if line_type == LineType.HEADING:
            self.handle_heading()
            return

        if line_type == LineType.SPECIFICATION:
            self.handle_specification()
            return

        if line_type == LineType.HEAD_DESCRIPTION:
            self.handle_head_description()
            return

        if line_type == LineType.MEASUREMENT_HEADER:
            self.handle_measurement_header()
            return

        if line_type == LineType.MEASUREMENT_ROW:
            self.handle_measurement_row()
            return

        if line_type == LineType.DEDUCTION:
            self.handle_deduction()
            return

        if line_type == LineType.LIST:
            self.handle_list()
            return

        if line_type == LineType.MATERIAL_ANALYSIS:
            self.handle_material_analysis()
            return

        if line_type == LineType.TOTAL:
            self.handle_total()
            return

        if line_type == LineType.SUMMARY:
            self.handle_summary()
            return

        self.handle_unknown()

    # ==========================================================

    @property
    def current_line(self):

        if self.index >= len(self.lines):
            return ""

        return self.lines[self.index]

    @property
    def previous_line(self):

        if self.index == 0:
            return ""

        return self.lines[self.index - 1]

    @property
    def next_line(self):

        if self.index + 1 >= len(self.lines):
            return ""

        return self.lines[self.index + 1]

    # ==========================================================

    def advance(self):

        self.index += 1

        self.context.next_line()

    # ==========================================================

    def eof(self):

        return self.index >= len(self.lines)

    # ==========================================================
    # Handlers
    # ==========================================================

    def handle_heading(self):
        raise NotImplementedError

    def handle_specification(self):
        raise NotImplementedError

    def handle_head_description(self):
        raise NotImplementedError

    def handle_measurement_header(self):
        raise NotImplementedError

    def handle_measurement_row(self):
        raise NotImplementedError

    def handle_deduction(self):
        raise NotImplementedError

    def handle_list(self):
        raise NotImplementedError

    def handle_material_analysis(self):
        raise NotImplementedError

    def handle_total(self):
        raise NotImplementedError

    def handle_summary(self):
        raise NotImplementedError

    def handle_unknown(self):
        raise NotImplementedError
