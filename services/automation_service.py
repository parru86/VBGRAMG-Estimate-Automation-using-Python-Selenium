"""
services/automation_service.py

Main Automation Service

Workflow

Estimate
    ↓
Appendix
    ↓
Specification
    ↓
Measurements

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from pages.appendix_page import AppendixPage
from pages.specification_page import SpecificationPage
from pages.activity_page import ActivityPage

from services.measurement_service import MeasurementService


class AutomationService:

    def __init__(self, browser):

        self.browser = browser

        self.appendix = AppendixPage(browser)

        self.specification = SpecificationPage(browser)

        self.activity = ActivityPage(browser)

        self.measurement = MeasurementService(browser)

    # ----------------------------------------------------------

    def create_appendix(self, estimate):

        """
        Create Analysis Of Rates Appendix
        """

        appendix_name = getattr(
            estimate,
            "appendix_name",
            "Analysis of Rates"
        )

        self.appendix.create_appendix(
            appendix_name
        )

    # ----------------------------------------------------------

    def add_specifications(self, estimate):

        """
        Add all Specification Codes
        """

        codes = []

        for item in estimate.items:

            codes.append(item.code)

        self.specification.add_all(codes)

    # ----------------------------------------------------------

    def add_measurements(self, estimate):

        """
        Fill measurements
        for every Specification.
        """

        for item in estimate.items:

            print(
                f"Opening Specification : {item.code}"
            )

            self.activity.open_measurements(
                item.code
            )

            self.measurement.process_item(
                item
            )

    # ----------------------------------------------------------

    def run(self, estimate):

        """
        Complete Automation
        """

        print("=" * 60)

        print("Creating Appendix...")

        self.create_appendix(
            estimate
        )

        print("Appendix Created.")

        print("=" * 60)

        print("Adding Specifications...")

        self.add_specifications(
            estimate
        )

        print("Specifications Added.")

        print("=" * 60)

        print("Adding Measurements...")

        self.add_measurements(
            estimate
        )

        print("Measurements Added.")

        print("=" * 60)

        print("Automation Completed Successfully.")

        print("=" * 60)