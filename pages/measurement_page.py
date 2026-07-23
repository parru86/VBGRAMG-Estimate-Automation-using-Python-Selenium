"""
pages/measurement_page.py

Measurement Page

Responsibilities
----------------
1. Open Measurement Dialog
2. Fill Measurement Fields
3. Add New Row
4. Save Measurements

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from pages.base_page import BasePage
from automation.locators import MeasurementPage as Locators


class MeasurementPage(BasePage):

    # --------------------------------------------------
     @staticmethod
    def add_measurement(specification_code):

        return (
            By.CSS_SELECTOR,
            f"span.addmessurbtn[data-divid*='_{specification_code}_']"
        )

    def open_measurements(self):

        self.click(
            Locators.ADD_MEASUREMENTS
        )

    # --------------------------------------------------

    def set_head_description(self, value: str):

        self.type(
            Locators.HEAD_DESCRIPTION,
            value,
        )

    # --------------------------------------------------

    def set_item_description(self, value: str):

        self.type(
            Locators.ITEM_DESCRIPTION,
            value,
        )

    # --------------------------------------------------

    def set_no(self, value):

        self.type(
            Locators.NUMBER,
            value,
        )

    # --------------------------------------------------

    def set_length(self, value):

        self.type(
            Locators.LENGTH,
            value,
        )

    # --------------------------------------------------

    def set_breadth(self, value):

        self.type(
            Locators.BREADTH,
            value,
        )

    # --------------------------------------------------

    def set_depth(self, value):

        self.type(
            Locators.DEPTH,
            value,
        )

    # --------------------------------------------------

    def set_cf(self, value):

        self.type(
            Locators.CF,
            value,
        )

    # --------------------------------------------------

    def add_row(self):

        self.js_click(
            Locators.ADD_ROW
        )

    # --------------------------------------------------

    def save(self):

        self.click(
            Locators.SAVE
        )

    # --------------------------------------------------

    def fill_row(self, measurement):

        """
        measurement object

        measurement.head_description

        measurement.item_description

        measurement.no

        measurement.length

        measurement.breadth

        measurement.depth

        measurement.cf
        """

        self.set_head_description(
            measurement.head_description
        )

        self.set_item_description(
            measurement.item_description
        )

        self.set_no(
            measurement.no
        )

        self.set_length(
            measurement.length
        )

        self.set_breadth(
            measurement.breadth
        )

        self.set_depth(
            measurement.depth
        )

        self.set_cf(
            measurement.cf
        )