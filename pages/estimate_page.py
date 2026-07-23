"""
Estimate Page

Handles:

1. Draft Estimate
2. Search Work
3. Select Work
4. Open Estimate

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

import time

from pages.base_page import BasePage

from selenium.locators import DashboardPage
from selenium.locators import EstimatePage as Locators


class EstimatePage(BasePage):

    # -------------------------------------------------

    def open_draft_estimate(self):

        self.click(
            DashboardPage.ESTIMATES_MENU
        )

        self.click(
            DashboardPage.DRAFT_ESTIMATE
        )

    # -------------------------------------------------

    def search_work(self, work_code: str):

        search_button = self.element(
            Locators.SEARCH_BUTTON
        )

        # Search box is not available.
        # Work list loads after clicking search.

        search_button.click()

        time.sleep(1)

    # -------------------------------------------------

    def select_work(self, work_code: str):

        rows = self.elements(
            Locators.WORK_ROWS
        )

        for row in rows:

            portal_code = row.get_attribute(
                "data-wcode"
            )

            if portal_code == work_code:

                self.driver.execute_script(
                    "arguments[0].click();",
                    row
                )

                return

        raise Exception(

            f"Estimate not found : {work_code}"

        )

    # -------------------------------------------------

    def click_edit(self):

        self.click(
            Locators.OPEN_ESTIMATE
        )

    # -------------------------------------------------

    def open_estimate(self, work_code: str):

        self.open_draft_estimate()

        self.search_work(work_code)

        self.select_work(work_code)

        self.click_edit()