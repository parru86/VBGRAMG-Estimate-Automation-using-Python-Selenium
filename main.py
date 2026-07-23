"""
VBGRAMG AUTO

Main Entry Point

Workflow

1. Manual Login
2. Manual Estimate Open
3. Press ENTER
4. Automation Starts
"""

from selenium.browser import Browser

from parser.estimate_parser import EstimateParser

from services.automation_service import AutomationService


# ---------------------------------------------------------

PDF_FILE = r"pdf/sample.pdf"

PORTAL_URL = "https://secure.dord.gov.in/securev2/"


# ---------------------------------------------------------

def main():

    print("=" * 60)
    print("VBGRAMG AUTO")
    print("=" * 60)

    print("\nReading Estimate PDF...")

    parser = EstimateParser()

    estimate = parser.parse(PDF_FILE)

    print("PDF Parsed Successfully.")

    browser = Browser()

    browser.open(PORTAL_URL)

    print("\n------------------------------------------------")

    print("Login Manually")

    print("Open Draft Estimate")

    print("Select Estimate")

    print("Click EDIT")

    print("------------------------------------------------")

    input("\nPress ENTER after Estimate Editor opens...")

    automation = AutomationService(browser)

    automation.run(estimate)

    print("\nAutomation Completed Successfully.")

    input("\nPress ENTER to Exit...")

    browser.close()


# ---------------------------------------------------------

if __name__ == "__main__":

    main()