"""
=========================================================
VBGRAMG AUTO ESTIMATE

MEASUREMENT PATTERN DETECTOR

=========================================================
"""

from enum import Enum, auto


class PatternType(Enum):

    UNKNOWN = auto()

    VOLUME = auto()

    AREA = auto()

    LENGTH = auto()

    WEIGHT = auto()

    COUNT = auto()


class MeasurementPattern:

    """
    Detect Measurement Pattern
    from numeric values.
    """

    @staticmethod
    def is_number(text):

        try:

            float(text)

            return True

        except:

            return False

    # --------------------------------------------------

    @classmethod
    def detect(cls, tokens):

        numbers = []

        for token in tokens:

            if cls.is_number(token):

                numbers.append(token)

        total = len(numbers)

        # --------------------------------------------

        if total >= 6:

            return PatternType.VOLUME

        if total == 5:

            return PatternType.AREA

        if total == 4:

            return PatternType.LENGTH

        if total == 3:

            return PatternType.WEIGHT

        if total == 2:

            return PatternType.COUNT

        return PatternType.UNKNOWN