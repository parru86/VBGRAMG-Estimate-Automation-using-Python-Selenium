"""
browser.py

Browser Manager for VBGRAMG Automation

Author : Parmeshwar Verma
Project : VBGRAMG_AUTO
"""

from __future__ import annotations

from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 20


class Browser:

    def __init__(
        self,
        driver_path: str | None = None,
        headless: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        download_dir: str = "output",
    ):

        self.timeout = timeout

        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

        chrome_options = Options()

        if headless:
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        prefs = {
            "download.default_directory": str(self.download_dir.resolve()),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
        }

        chrome_options.add_experimental_option(
            "prefs",
            prefs,
        )

        if driver_path:
            service = Service(driver_path)
            self.driver: WebDriver = webdriver.Chrome(
                service=service,
                options=chrome_options,
            )
        else:
            self.driver = webdriver.Chrome(
                options=chrome_options
            )

        self.wait = WebDriverWait(
            self.driver,
            timeout,
        )

    # ------------------------------------------------

    def open(self, url: str):

        self.driver.get(url)

    # ------------------------------------------------

    def maximize(self):

        self.driver.maximize_window()

    # ------------------------------------------------

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    # ------------------------------------------------

    def js_click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element,
        )

    # ------------------------------------------------

    def type(self, locator, value):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(str(value))

    # ------------------------------------------------

    def clear(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

    # ------------------------------------------------

    def get(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # ------------------------------------------------

    def gets(self, locator):

        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # ------------------------------------------------

    def visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # ------------------------------------------------

    def invisible(self, locator):

        return self.wait.until(
            EC.invisibility_of_element(locator)
        )

    # ------------------------------------------------

    def exists(self, locator):

        try:

            self.wait.until(
                EC.presence_of_element_located(locator)
            )

            return True

        except TimeoutException:

            return False

    # ------------------------------------------------

    def scroll_to(self, locator):

        element = self.get(locator)

        self.driver.execute_script(

            "arguments[0].scrollIntoView({block:'center'});",

            element,

        )

    # ------------------------------------------------

    def screenshot(self, filename):

        path = self.download_dir / filename

        self.driver.save_screenshot(str(path))

        return path

    # ------------------------------------------------

    def close(self):

        self.driver.quit()