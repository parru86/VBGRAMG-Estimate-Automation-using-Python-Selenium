"""
services/measurement_service.py

Business Logic

Measurement Automation

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from pages.measurement_page import MeasurementPage


class MeasurementService:

    def __init__(self, browser):

        self.page = MeasurementPage(browser)

    # --------------------------------------------------------

    def fill_measurement(self, measurement):

        """
        Fill one measurement row.

        Parameters
        ----------

        measurement :
            Measurement Model
        """

        self.page.fill_row(
            measurement
        )

    # --------------------------------------------------------

    def fill_all_measurements(
        self,
        item,
    ):

        """
        Fill all measurements
        of one specification.

        item.measurements
        """

        self.page.open_measurements()

        total = len(item.measurements)

        for index, measurement in enumerate(item.measurements):

            self.fill_measurement(
                measurement
            )

            # Add next row only
            # if another measurement exists

            if index < total - 1:

                self.page.add_row()

        self.page.save()

    # --------------------------------------------------------

    def process_item(
        self,
        item,
    ):

        """
        Fill one Specification.

        Example

        79.01.01
        """

        self.fill_all_measurements(
            item
        )

    # --------------------------------------------------------

    def process_estimate(
        self,
        estimate,
    ):

        """
        estimate.items

        Loop all specifications.
        """

        for item in estimate.items:

            self.process_item(
                item
            )