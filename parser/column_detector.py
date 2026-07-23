"""
=========================================================
VBGRAMG AUTO ESTIMATE
COLUMN DETECTOR
=========================================================
"""

from dataclasses import dataclass


@dataclass
class Column:

    name: str

    x: float


class ColumnDetector:

    """
    Detect Measurement Table Columns
    """

    REQUIRED_COLUMNS = [

        "Sl",

        "Description",

        "No",

        "L",

        "B",

        "D",

        "CF",

        "Quantity"

    ]

    # --------------------------------------------------

    def detect(self, row):

        """
        row = Row Object

        Return:

        {
            "Sl":35.14,
            "Description":84.85,
            ...
        }
        """

        columns = {}

        for word in row.words:

            txt = word["text"]

            if txt in self.REQUIRED_COLUMNS:

                columns[txt] = Column(

                    name=txt,

                    x=round(word["x0"], 2)

                )

        return columns

    # --------------------------------------------------

    def nearest_column(self, x, columns):

        """
        Find nearest column according to x position
        """

        nearest = None

        distance = 99999

        for column in columns.values():

            d = abs(column.x - x)

            if d < distance:

                distance = d

                nearest = column.name

        return nearest

    # --------------------------------------------------

    def print(self, columns):

        print()

        print("Detected Columns")

        print("-" * 40)

        for c in columns.values():

            print(

                f"{c.name:12} : {c.x}"

            )