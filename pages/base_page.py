"""
pages/base_page.py

Base Page Class

All Page Objects inherit from this class.

Project:
VBGRAMG_AUTO
"""

from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):

        self.browser = browser
        self.driver = browser.driver
        self.wait = browser.wait

    # --------------------------------------------------------

    def element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # --------------------------------------------------------

    def elements(self, locator):

        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # --------------------------------------------------------

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    # --------------------------------------------------------

    def js_click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # --------------------------------------------------------

    def safe_click(self, locator):
        """
        Most reliable click method.

        1.Scroll
        2.JavaScript Click
        """

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # --------------------------------------------------------

    def type(self, locator, value):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(str(value))

    # --------------------------------------------------------

    def clear(self, locator):

        self.wait.until(
            EC.visibility_of_element_located(locator)
        ).clear()

    # --------------------------------------------------------

    def text(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    # --------------------------------------------------------

    def attribute(self, locator, name):

        return self.element(locator).get_attribute(name)

    # --------------------------------------------------------

    def exists(self, locator):

        try:

            self.element(locator)

            return True

        except TimeoutException:

            return False

    # --------------------------------------------------------

    def scroll(self, locator):

        element = self.element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

    # --------------------------------------------------------

    def hover(self, locator):

        ActionChains(self.driver).move_to_element(
            self.element(locator)
        ).perform()

    # --------------------------------------------------------

    def screenshot(self, filename):

        self.driver.save_screenshot(filename)

    # --------------------------------------------------------

    def wait_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # --------------------------------------------------------

    def wait_clickable(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )