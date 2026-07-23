from automation.browser import Browser
from pages.specification_page import SpecificationPage

PORTAL_URL = "https://secure.dord.gov.in/securev2/"

browser = Browser()

browser.open(PORTAL_URL)

input("""
Manual Steps

1. Login
2. Open Draft Estimate
3. Select Estimate
4. Click Edit
5. Create Appendix (dabari)
6. Press ENTER...
""")

page = SpecificationPage(browser)

page.add_all([
    "79.01.01",
    "79.01.02",
    "79.01.07"
])

print("Specification Added Successfully.")

input("Press ENTER to Close...")

browser.close()