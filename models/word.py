"""
=========================================================
VBGRAMG AUTO ESTIMATE
WORD MODEL
=========================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Word:
    """
    Represents a single word extracted from PDF.
    """

    page: int

    text: str

    x0: float

    x1: float

    top: float

    bottom: float

    @property
    def width(self) -> float:
        return round(self.x1 - self.x0, 2)

    @property
    def height(self) -> float:
        return round(self.bottom - self.top, 2)

    @property
    def center(self) -> float:
        return round((self.x0 + self.x1) / 2, 2)

    def __repr__(self):

        return (

            f"Word('{self.text}', "

            f"x={self.x0:.2f}, "

            f"y={self.top:.2f})"

        )