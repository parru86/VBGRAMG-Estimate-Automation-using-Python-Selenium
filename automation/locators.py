"""
VBGRAMG Portal Locators

Author : Parmeshwar Verma
Project : VBGRAMG_AUTO
"""

from selenium.webdriver.common.by import By


# ----------------------------------------------------------
# Landing Page
# ----------------------------------------------------------

class LandingPage:

    LOGIN_HERE = (
        By.XPATH,
        "//a[contains(normalize-space(),'LOGIN HERE')]"
    )


# ----------------------------------------------------------
# Login Page
# ----------------------------------------------------------

class LoginPage:

    USERNAME = (
        By.ID,
        "susername"
    )

    PASSWORD = (
        By.ID,
        "spassword"
    )

    CAPTCHA = (
        By.ID,
        "capcha"
    )

    CAPTCHA_IMAGE = (
        By.ID,
        "captchaimg"
    )

    CAPTCHA_REFRESH = (
        By.ID,
        "btncapchrefresh"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )


# ----------------------------------------------------------
# Dashboard
# ----------------------------------------------------------

class DashboardPage:

    ESTIMATES_MENU = (
        By.XPATH,
        "//span[normalize-space()='Estimates']"
    )

    DRAFT_ESTIMATE = (
        By.XPATH,
        "//span[normalize-space()='Draft Estimate']"
    )


# ----------------------------------------------------------
# Estimate Page
# ----------------------------------------------------------

class EstimatePage:

    SEARCH_BUTTON = (
        By.ID,
        "searchestimate"
    )

    WORK_ROWS = (
        By.CSS_SELECTOR,
        "div.media.active-media-list"
    )

    OPEN_ESTIMATE = (
        By.ID,
        "openEstimate"
    )


# ----------------------------------------------------------
# Appendix
# ----------------------------------------------------------

class AppendixPage:

    ADD_APPENDIX = (
        By.CSS_SELECTOR,
    "div.btnAddapp"
    )

    ANALYSIS_TEXTBOX = (
        By.ID,
        "est_desc"
    )

    ADD_BUTTON = (
        By.ID,
        "desc_save_button"
    )


# ----------------------------------------------------------
# Specification
# ----------------------------------------------------------

class SpecificationPage:

    ADD_SPECIFICATION = (
        By.CSS_SELECTOR,
        "i[title='Add Specification']"
    )

    SUBHEAD = (
        By.ID,
        "select2-sel_subhead-container"
    )

    SEARCH_BOX = (
        By.XPATH,
        "//input[@placeholder='Search Specification Code / Specification Description']"
    )

    SEARCH_BUTTON = (
        By.ID,
        "button-search"
    )

    SAVE = (
        By.ID,
        "specSaveButton"
    )

    @staticmethod
    def checkbox(specification_code: str):

        return (
            By.CSS_SELECTOR,
            f"input[data-id='{specification_code}']"
        )


# ----------------------------------------------------------
# Measurement
# ----------------------------------------------------------

class MeasurementPage:

    @staticmethod
    def add_measurement(specification_code):

    return (
        By.CSS_SELECTOR,
        f"span.addmessurbtn[data-divid*='_{specification_code}_']"
    )

    HEAD_DESCRIPTION = (
        By.CSS_SELECTOR,
        "input.calspecdec"
    )

    ITEM_DESCRIPTION = (
        By.CSS_SELECTOR,
        "input.itmd_desc"
    )

    NUMBER = (
        By.CSS_SELECTOR,
        "input.item_no"
    )

    LENGTH = (
        By.CSS_SELECTOR,
        "input.item_length"
    )

    BREADTH = (
        By.CSS_SELECTOR,
        "input.item_breadth"
    )

    DEPTH = (
        By.CSS_SELECTOR,
        "input.item_depth"
    )

    CF = (
        By.CSS_SELECTOR,
        "input.item_cf"
    )

    ADD_ROW = (
        By.CSS_SELECTOR,
        "span.addrow"
    )

    SAVE = (
        By.CSS_SELECTOR,
        "span.savemessurbtn"
    )