from selenium.webdriver.common.by import By

from automation.browser import Browser
from pages.activity_page import ActivityPage


browser = Browser()

browser.open("https://secure.dord.gov.in/securev2/")

input("""
========================================

1. Login

2. Open Draft Estimate

3. Click Edit

4. Add Appendix

5. Add Specification

6. Make sure Activity (+) icons are visible

7. Press ENTER

========================================
""")

print("\nChecking Measurement Icons...\n")

icons = browser.driver.find_elements(
    By.CSS_SELECTOR,
    "i.measurement-view"
)

print("=" * 60)
print("Measurement Icons Found :", len(icons))
print("=" * 60)

for i, icon in enumerate(icons, start=1):

    print(
        i,
        " -> ",
        icon.get_attribute("data-viewid")
    )

print("=" * 60)

activity = ActivityPage(browser)

activity.open_measurements("79.01.01")

print("\n✅ Measurement Dialog Opened Successfully.")

input("\nPress ENTER to Close Browser...")

browser.close()