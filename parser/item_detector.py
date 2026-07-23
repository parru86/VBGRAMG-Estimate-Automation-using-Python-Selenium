"""
=========================================================
VBGRAMG AUTO ESTIMATE
ITEM DETECTOR
=========================================================
"""

from __future__ import annotations

from enum import Enum, auto
from typing import List, Optional

from models.row import Row
from models.item_block import ItemBlock


# =========================================================
# PARSER STATE
# =========================================================

class ParseState(Enum):

    SEARCH_ITEM = auto()

    READ_DESCRIPTION = auto()

    READ_MEASUREMENTS = auto()

    READ_RATE_ANALYSIS = auto()


# =========================================================
# ITEM DETECTOR
# =========================================================

class ItemDetector:

    """
    Convert PDF Rows into ItemBlocks.

    Input
    -----
    List[Row]

    Output
    ------
    List[ItemBlock]
    """

    def __init__(self):

        self.blocks: List[ItemBlock] = []

        self.current: Optional[ItemBlock] = None

        self.state = ParseState.SEARCH_ITEM

        self.row_index = 0

    # -----------------------------------------------------

    def detect(self, rows: List[Row]) -> List[ItemBlock]:

        """
        Main Parser
        """

        # reset

        self.blocks.clear()

        self.current = None

        self.state = ParseState.SEARCH_ITEM

        for index, row in enumerate(rows):

            self.row_index = index

            # ---------------------------------------------
            # SEARCH NEW ITEM
            # ---------------------------------------------

            if self.state == ParseState.SEARCH_ITEM:

                if self._is_item(row):

                    self._start_item(row)

                    self.state = ParseState.READ_DESCRIPTION

                continue

            # ---------------------------------------------
            # DESCRIPTION
            # ---------------------------------------------

            if self.state == ParseState.READ_DESCRIPTION:

                if self._is_item(row):

                    self._close_item()

                    self._start_item(row)

                    continue

                if self._is_header(row):

                    self.current.add_row(row)

                    self.state = ParseState.READ_MEASUREMENTS

                    continue

                self.current.add_row(row)

                continue

            # ---------------------------------------------
            # MEASUREMENTS
            # ---------------------------------------------

            if self.state == ParseState.READ_MEASUREMENTS:

                if self._is_item(row):

                    self._close_item()

                    self._start_item(row)

                    self.state = ParseState.READ_DESCRIPTION

                    continue

                if self._is_list(row):

                    self.current.add_row(row)

                    self.state = ParseState.READ_RATE_ANALYSIS

                    continue

                self.current.add_row(row)

                if self._is_measurement(row):

                    self.current.add_measurement_row(row)

                continue

            # ---------------------------------------------
            # RATE ANALYSIS
            # ---------------------------------------------

            if self.state == ParseState.READ_RATE_ANALYSIS:

                if self._is_item(row):

                    self._close_item()

                    self._start_item(row)

                    self.state = ParseState.READ_DESCRIPTION

                    continue

                self.current.add_row(row)

                self.current.add_rate_row(row)

        # Last Item

        self._close_item()

        return self.blocks
    # -----------------------------------------------------

    def _start_item(self, row: Row):

        """
        Create new ItemBlock from Item Row.
        """

        item_no, item_code, description = self._extract_item_info(row)

        self.current = ItemBlock(

            item_no=item_no,

            item_code=item_code,

            description=description,

            start_page=row.page,

            end_page=row.page,

            start_row=self.row_index,

            end_row=self.row_index

        )

        self.current.add_row(row)

    # -----------------------------------------------------

    def _close_item(self):

        """
        Finish current ItemBlock.
        """

        if self.current is None:
            return

        self.current.end_row = self.row_index

        if self.current.rows:
            self.current.end_page = self.current.rows[-1].page

        self.blocks.append(self.current)

        self.current = None

    # -----------------------------------------------------

    def _extract_item_info(self, row: Row):

        """
        Example

        1 79.03.01b -- Earth work ....

        Returns

        (1, "79.03.01b", "Earth work ....")
        """

        words = row.text.split()

        item_no = int(words[0])

        item_code = words[1]

        description = " ".join(words[3:]).strip()

        return item_no, item_code, description

    # -----------------------------------------------------

    def _is_item(self, row: Row):

        return row.is_item()

    # -----------------------------------------------------

    def _is_header(self, row: Row):

        return row.is_header()

    # -----------------------------------------------------

    def _is_measurement(self, row: Row):

        return row.is_measurement()

    # -----------------------------------------------------

    def _is_list(self, row: Row):

        return row.is_list()    