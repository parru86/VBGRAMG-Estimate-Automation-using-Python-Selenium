"""
Base Page Class

All portal pages inherit this class.

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

    # --------------------------------------------------

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    # --------------------------------------------------

    def js_click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # --------------------------------------------------

    def type(self, locator, value):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(str(value))

    # --------------------------------------------------

    def clear(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

    # --------------------------------------------------

    def read(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    # --------------------------------------------------

    def element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # --------------------------------------------------

    def elements(self, locator):

        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # --------------------------------------------------

    def exists(self, locator):

        try:

            self.element(locator)

            return True

        except TimeoutException:

            return False

    # --------------------------------------------------

    def visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # --------------------------------------------------

    def invisible(self, locator):

        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    # --------------------------------------------------

    def scroll(self, locator):

        element = self.element(locator)

        self.driver.execute_script(

            "arguments[0].scrollIntoView({block:'center'});",

            element,

        )

    # --------------------------------------------------

    def hover(self, locator):

        element = self.element(locator)

        ActionChains(self.driver).move_to_element(element).perform()

    # --------------------------------------------------

    def attribute(self, locator, name):

        return self.element(locator).get_attribute(name)

    # --------------------------------------------------

    def screenshot(self, filename):

        return self.browser.screenshot(filename)