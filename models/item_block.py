"""
=========================================================
VBGRAMG AUTO ESTIMATE
ITEM BLOCK MODEL
=========================================================

Temporary Parser Object

PDF
 ↓
ItemBlock
 ↓
Item
=========================================================
"""

from dataclasses import dataclass, field
from typing import List

from models.row import Row


@dataclass(slots=True)
class ItemBlock:
    """
    Represents one Item Block extracted from PDF.

    Example:

        79.03.01b
        Description...
        Measurement Rows
        LIST
        Rate Analysis
        Total Qty

    """

    # Item Information

    item_no: int

    item_code: str

    description: str = ""

    # PDF Location

    start_page: int = 0

    end_page: int = 0

    start_row: int = 0

    end_row: int = 0

    # Raw Rows

    rows: List[Row] = field(default_factory=list)

    # Measurement Area

    measurement_rows: List[Row] = field(default_factory=list)

    # Rate Analysis Area

    rate_rows: List[Row] = field(default_factory=list)

    # -----------------------------------------------------

    def add_row(self, row: Row):

        self.rows.append(row)

    # -----------------------------------------------------

    def add_measurement_row(self, row: Row):

        self.measurement_rows.append(row)

    # -----------------------------------------------------

    def add_rate_row(self, row: Row):

        self.rate_rows.append(row)

    # -----------------------------------------------------

    @property
    def row_count(self):

        return len(self.rows)

    # -----------------------------------------------------

    @property
    def measurement_count(self):

        return len(self.measurement_rows)

    # -----------------------------------------------------

    @property
    def rate_count(self):

        return len(self.rate_rows)

    # -----------------------------------------------------

    def clear(self):

        self.rows.clear()

        self.measurement_rows.clear()

        self.rate_rows.clear()

    # -----------------------------------------------------

    def __repr__(self):

        return (

            f"ItemBlock("

            f"{self.item_code}, "

            f"Rows={self.row_count}, "

            f"Measurements={self.measurement_count}"

            f")"

        )