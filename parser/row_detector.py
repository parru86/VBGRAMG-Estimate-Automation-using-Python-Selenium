"""
=========================================================
VBGRAMG AUTO ESTIMATE
ROW DETECTOR
=========================================================
"""

from models.row import Row


class RowDetector:

    """
    Convert PDF Words into Row Objects
    """

    def __init__(self, tolerance=2):

        self.tolerance = tolerance

    # ----------------------------------------------------

    def detect(self, words):

        rows = []

        current = []

        current_top = None

        for word in words:

            if current_top is None:

                current_top = word.top

            if abs(word.top - current_top) <= self.tolerance:

                current.append(word)

            else:

                row = Row(

                    page=current[0].page,

                    top=current[0].top,

                    bottom=current[0].bottom

                )

                for w in current:

                    row.add_word(w)

                row.sort()

                rows.append(row)

                current = [word]

                current_top = word.top

        if current:

            row = Row(

                page=current[0].page,

                top=current[0].top,

                bottom=current[0].bottom

            )

            for w in current:

                row.add_word(w)

            row.sort()

            rows.append(row)

        return rows

    # ----------------------------------------------------

    def detect_all(self, pages):

        all_rows = []

        for page in pages:

            all_rows.extend(

                self.detect(page)

            )

        return all_rows