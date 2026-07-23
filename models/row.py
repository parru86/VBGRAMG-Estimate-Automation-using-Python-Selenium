"""
=========================================================
VBGRAMG AUTO ESTIMATE
ROW MODEL
=========================================================
"""

from dataclasses import dataclass, field
from typing import List
import re

from models.word import Word


@dataclass(slots=True)
class Row:
    """
    Represents one complete row extracted from PDF.
    """

    page: int

    top: float

    bottom: float

    words: List[Word] = field(default_factory=list)

    # Item Pattern
    ITEM_PATTERN = re.compile(
        r'^\d+\s+79\.[A-Za-z0-9\.]+\s+--'
    )

    # --------------------------------------------------

    @property
    def text(self) -> str:
        """
        Complete row text.
        """
        return " ".join(word.text for word in self.words)

    # --------------------------------------------------

    @property
    def left(self) -> float:

        if not self.words:
            return 0.0

        return min(word.x0 for word in self.words)

    # --------------------------------------------------

    @property
    def right(self) -> float:

        if not self.words:
            return 0.0

        return max(word.x1 for word in self.words)

    # --------------------------------------------------

    @property
    def width(self) -> float:

        return round(self.right - self.left, 2)

    # --------------------------------------------------

    @property
    def word_count(self) -> int:

        return len(self.words)

    # --------------------------------------------------

    def add_word(self, word: Word):

        self.words.append(word)

    # --------------------------------------------------

    def sort(self):

        self.words.sort(key=lambda w: w.x0)

    # --------------------------------------------------

    def is_empty(self):

        return len(self.words) == 0

    # --------------------------------------------------

    def is_item(self):

        """
        Detect Estimate Item Row

        Example:
        1 79.03.01b -- Earth Work...
        """

        return bool(

            self.ITEM_PATTERN.match(self.text)

        )

    # --------------------------------------------------

    def is_header(self):

        """
        Measurement Table Header
        """

        return self.text.startswith(

            "Sl No Description"

        )

    # --------------------------------------------------

    def is_list(self):

        """
        LIST Row
        """

        return self.text.strip() == "LIST"

    # --------------------------------------------------

    def is_total(self):

        """
        Total Quantity Row
        """

        return self.text.startswith(

            "Total"

        )

    # --------------------------------------------------

    def is_measurement(self):

        """
        Detect Measurement Row

        Example

        1 - 3.14 3.350 0.450 0.450 1.0 2.1300 -

        OR

        1 1 1 6.430 1.0 6.4300 -
        """

        if self.word_count < 6:
            return False

        try:

            int(self.words[0].text)

            return True

        except ValueError:

            return False

    # --------------------------------------------------

    def __repr__(self):

        return (

            f"Row("

            f"Page={self.page}, "

            f"Words={self.word_count}, "

            f"Text='{self.text[:60]}'"

            f")"

        )