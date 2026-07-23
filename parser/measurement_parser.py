"""
=========================================================
VBGRAMG AUTO ESTIMATE
MEASUREMENT PARSER
=========================================================
"""

from __future__ import annotations

import re
from typing import List

from models.item_block import ItemBlock
from models.measurement import Measurement
from parser.measurement_patterns import (
    MeasurementPattern,
    PatternType,
)


class MeasurementParser:

    NUMBER_PATTERN = re.compile(
        r"^-?\d+(?:\.\d+)?$"
    )

    # --------------------------------------------------

    def parse(
        self,
        block: ItemBlock
    ) -> List[Measurement]:

        measurements = []

        for row in block.measurement_rows:

            m = self._parse_row(row)

            if m is not None:
                measurements.append(m)

        return measurements

    # --------------------------------------------------

    def _parse_row(self, row):

        tokens = [
            w.text.strip()
            for w in row.words
            if w.text.strip()
        ]

        if not tokens:
            return None

        return self._build_measurement(tokens)

    # --------------------------------------------------

    def _build_measurement(self, tokens):

        numbers = []
        text = []

        for token in tokens:

            if self._is_number(token):
                numbers.append(float(token))
            elif token != "-":
                text.append(token)

        if len(numbers) < 2:
            return None

        pattern = MeasurementPattern.detect(tokens)

        sl = int(numbers[0])

        quantity = numbers[-1]

        values = numbers[1:-1]

        description = " ".join(text)

        measurement = Measurement(

            sl=sl,

            description=description,

            quantity=quantity

        )

        # Pattern Based Parsing

        if pattern == PatternType.VOLUME:

            self._parse_volume(
                measurement,
                values
            )

        elif pattern == PatternType.AREA:

            self._parse_area(
                measurement,
                values
            )

        elif pattern == PatternType.LENGTH:

            self._parse_length(
                measurement,
                values
            )

        elif pattern == PatternType.WEIGHT:

            self._parse_weight(
                measurement,
                values
            )

        elif pattern == PatternType.COUNT:

            self._parse_count(
                measurement,
                values
            )

        return measurement
    # --------------------------------------------------

    def _parse_volume(
        self,
        measurement,
        values
    ):

        if len(values) >= 1:
            measurement.no = values[0]

        if len(values) >= 2:
            measurement.length = values[1]

        if len(values) >= 3:
            measurement.breadth = values[2]

        if len(values) >= 4:
            measurement.depth = values[3]

        if len(values) >= 5:
            measurement.cf = values[4]

    # --------------------------------------------------

    def _parse_area(
        self,
        measurement,
        values
    ):

        if len(values) >= 1:
            measurement.no = values[0]

        if len(values) >= 2:
            measurement.length = values[1]

        if len(values) >= 3:
            measurement.breadth = values[2]

        if len(values) >= 4:
            measurement.cf = values[3]

    # --------------------------------------------------

    def _parse_length(
        self,
        measurement,
        values
    ):

        if len(values) >= 1:
            measurement.no = values[0]

        if len(values) >= 2:
            measurement.length = values[1]

        if len(values) >= 3:
            measurement.cf = values[2]

    # --------------------------------------------------

    def _parse_weight(
        self,
        measurement,
        values
    ):

        if len(values) >= 1:
            measurement.length = values[0]

        if len(values) >= 2:
            measurement.breadth = values[1]

        if len(values) >= 3:
            measurement.cf = values[2]

    # --------------------------------------------------

    def _parse_count(
        self,
        measurement,
        values
    ):

        if len(values) >= 1:
            measurement.no = values[0]

    # --------------------------------------------------

    @classmethod
    def _is_number(
        cls,
        text
    ):

        return bool(
            cls.NUMBER_PATTERN.match(text)
        )    