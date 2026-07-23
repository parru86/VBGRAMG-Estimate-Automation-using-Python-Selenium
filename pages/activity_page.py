"""
pages/activity_page.py
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ActivityPage(BasePage):
    """
    Handles Activity (+) and Add Measurements actions.
    """

    def activity_locator(self, specification_code: str):
        return (
            By.CSS_SELECTOR,
            f"i.measurement-view[data-viewid*='_{specification_code}_']"
        )

    def add_measurement_locator(self, specification_code: str):
        return (
            By.CSS_SELECTOR,
            f"span.addmessurbtn[data-divid*='_{specification_code}_']"
        )

    def expand_activity(self, specification_code: str):
        print("Searching locator:", self.activity_locator(specification_code))
        """
        Click Activity (+)
        """

        locator = self.activity_locator(specification_code)

        print(f"[Activity] Expanding : {specification_code}")

        self.safe_click(locator)

    def wait_for_add_measurement(self, specification_code: str):
        """
        Wait until Add Measurement button becomes clickable.
        """

        locator = self.add_measurement_locator(specification_code)

        self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click_add_measurement(self, specification_code: str):
        """
        Click Add Measurement button.
        """

        locator = self.add_measurement_locator(specification_code)

        print(f"[Measurement] Opening : {specification_code}")

        self.safe_click(locator)

    def open_measurements(self, specification_code: str):
        """
        Complete workflow:
            Activity +
                ↓
            Wait
                ↓
            Add Measurement
        """

        self.expand_activity(specification_code)

        self.wait_for_add_measurement(specification_code)

        self.click_add_measurement(specification_code)

        print("[OK] Measurement dialog opened.")