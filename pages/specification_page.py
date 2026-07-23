"""
pages/specification_page.py

VBGRAMG Specification Page

Responsibilities

1. Add Specification
2. Select Sub Head
3. Tick Specification Checkbox
4. Save

Project : VBGRAMG_AUTO
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from automation.locators import SpecificationPage as Locators


class SpecificationPage(BasePage):

    SUBHEAD_NAME = "79 - MGNREGA Chathisgarh Data"

    # --------------------------------------------------------

    def click_add_specification(self):

        self.safe_click(
            Locators.ADD_SPECIFICATION
        )

    # --------------------------------------------------------

    def select_subhead(self):

        self.safe_click(
            Locators.SUBHEAD
        )

        option = (
            By.XPATH,
            f"//li[contains(normalize-space(),'{self.SUBHEAD_NAME}')]"
        )

        self.safe_click(option)

    # --------------------------------------------------------

    def select_checkbox(self, specification_code):

        locator = Locators.checkbox(
            specification_code
        )

        checkbox = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkbox
        )

        if not checkbox.is_selected():

            self.driver.execute_script(
                "arguments[0].click();",
                checkbox
            )

    # --------------------------------------------------------

    def save(self):

        self.safe_click(
            Locators.SAVE
        )

    # --------------------------------------------------------

    def add_all(self, specification_codes):

        self.click_add_specification()

        self.select_subhead()

        unique_codes = sorted(
            {
                code.strip()
                for code in specification_codes
            }
        )

        for code in unique_codes:

            print(f"Selecting : {code}")

            self.select_checkbox(code)

        self.save()

        print("Specifications Saved.")