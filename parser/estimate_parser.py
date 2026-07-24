"""
parser/estimate_parser.py

VBGRAMG Estimate Parser

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from pathlib import Path
import re

from models.estimate import Estimate

from parser.pdf_reader import PDFReader
from parser.normalizer import TextNormalizer
from parser.line_classifier import (
    LineClassifier,
    LineType,
)
from parser.row_parser import RowParser
from parser.row_buffer import RowBuffer
from parser.estimate_builder import EstimateBuilder
from parser.state_machine import (
    ParserContext,
    ParserState,
    ParseMode,
)


class EstimateParser:

    SPEC_PATTERN = re.compile(
        r"^\d+\s+([0-9A-Za-z.]+)\s+--\s+(.*)$"
    )

    def __init__(self):

        self.reader = PDFReader()

        self.normalizer = TextNormalizer()

        self.classifier = LineClassifier()

        self.row_parser = RowParser()

        self.row_buffer = RowBuffer()

        self.builder = EstimateBuilder()

        self.context = ParserContext()

        self.lines: list[str] = []

        self.index = 0

    # =====================================================
    # PUBLIC
    # =====================================================

    def parse(
        self,
        pdf_path: str | Path,
    ) -> Estimate:

        self.reset()

        text = self.reader.read(pdf_path)

        self.lines = self.normalizer.normalize(text)

        self.parse_lines()

        return self.finish()

    # =====================================================

    def reset(self):

        self.builder.reset()

        self.context = ParserContext()

        self.row_buffer.clear()

        self.lines = []

        self.index = 0

    # =====================================================

    @property
    def current_line(self):

        if self.index >= len(self.lines):

            return ""

        return self.lines[self.index]

    # =====================================================

    @property
    def previous_line(self):

        if self.index == 0:

            return ""

        return self.lines[self.index - 1]

    # =====================================================

    @property
    def next_line(self):

        if self.index + 1 >= len(self.lines):

            return ""

        return self.lines[self.index + 1]

    # =====================================================

    def eof(self):

        return self.index >= len(self.lines)

    # =====================================================

    def advance(self):

        self.index += 1

        self.context.next_line()

    # =====================================================
    # MAIN LOOP
    # =====================================================

    def parse_lines(self):

        while not self.eof():

            line_type = self.classifier.classify(
                self.current_line
            )

            self.dispatch(line_type)

            self.advance()

    # =====================================================

    def dispatch(
        self,
        line_type: LineType,
    ):

        handlers = {

            LineType.HEADING:
                self.handle_heading,

            LineType.SPECIFICATION:
                self.handle_specification,

            LineType.HEAD_DESCRIPTION:
                self.handle_head_description,

            LineType.MEASUREMENT_HEADER:
                self.handle_measurement_header,

            LineType.MEASUREMENT_ROW:
                self.handle_measurement_row,

            LineType.DEDUCTION:
                self.handle_deduction,

            LineType.LIST:
                self.handle_list,

            LineType.MATERIAL_ANALYSIS:
                self.handle_material_analysis,

            LineType.TOTAL:
                self.handle_total,

            LineType.SUMMARY:
                self.handle_summary,

            LineType.EMPTY:
                self.handle_empty,

            LineType.UNKNOWN:
                self.handle_unknown,
        }

        handler = handlers.get(
            line_type,
            self.handle_unknown,
        )

        handler()

    # =====================================================
    # HANDLERS
    # =====================================================

    def handle_heading(self):
        raise NotImplementedError()

    def handle_specification(self):
        raise NotImplementedError()

    def handle_head_description(self):
        raise NotImplementedError()

    def handle_measurement_header(self):
        raise NotImplementedError()

    def handle_measurement_row(self):
        raise NotImplementedError()

    def handle_deduction(self):
        raise NotImplementedError()

    def handle_list(self):
        raise NotImplementedError()

    def handle_material_analysis(self):
        raise NotImplementedError()

    def handle_total(self):
        raise NotImplementedError()

    def handle_summary(self):
        raise NotImplementedError()

    def handle_empty(self):
        pass

    def handle_unknown(self):
        pass

    # =====================================================

    def finish(self) -> Estimate:

        self.builder.close_specification()

        self.context.finish()

        return self.builder.get_estimate()