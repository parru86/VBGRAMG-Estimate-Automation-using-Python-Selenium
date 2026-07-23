from pages.base_page import BasePage
from selenium.locators import LandingPage
from selenium.locators import LoginPage as LoginLocators


class LoginPage(BasePage):

    def open_login_popup(self):

        self.click(LandingPage.LOGIN_HERE)

    def enter_username(self, username):

        self.type(
            LoginLocators.USERNAME,
            username,
        )

    def enter_password(self, password):

        self.type(
            LoginLocators.PASSWORD,
            password,
        )

    def wait_for_manual_captcha(self):

        input(
            "\nEnter CAPTCHA manually and press ENTER..."
        )

    def click_login(self):

        self.click(
            LoginLocators.LOGIN_BUTTON
        )

    def login(self, username, password):

        self.open_login_popup()

        self.enter_username(username)

        self.enter_password(password)

        print("\nPlease enter CAPTCHA...")

        self.wait_for_manual_captcha()

        self.click_login()