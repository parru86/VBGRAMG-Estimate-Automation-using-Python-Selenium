"""
pages/appendix_page.py

Appendix Page

Responsibilities
----------------
1. Click Add Appendix
2. Enter Appendix Name
3. Click Add
4. Wait until Appendix is created

Project : VBGRAMG_AUTO
"""

from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from automation.locators import AppendixPage as Locators


class AppendixPage(BasePage):

    DEFAULT_APPENDIX_NAME = "Analysis of Rates"

    # --------------------------------------------------

    def click_add_appendix(self):

        def click_add_appendix(self):

    self.safe_click(
        Locators.ADD_APPENDIX
    )

    # --------------------------------------------------

    def enter_appendix_name(
        self,
        appendix_name: str,
    ):

        self.type(
            Locators.ANALYSIS_TEXTBOX,
            appendix_name,
        )

    # --------------------------------------------------

    def click_add(self):

        self.click(
            Locators.ADD_BUTTON
        )

    # --------------------------------------------------

    def wait_until_created(self):

        """
        Wait until popup textbox disappears.

        If textbox is still visible,
        Appendix creation is assumed failed.
        """

        self.wait.until(
            EC.invisibility_of_element_located(
                Locators.ANALYSIS_TEXTBOX
            )
        )

    # --------------------------------------------------

    def create_appendix(
        self,
        appendix_name: str | None = None,
    ):

        if appendix_name is None:

            appendix_name = self.DEFAULT_APPENDIX_NAME

        self.click_add_appendix()

        self.enter_appendix_name(
            appendix_name
        )

        self.click_add()

        self.wait_until_created()

        return True