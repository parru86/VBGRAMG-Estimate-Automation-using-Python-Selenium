from automation.browser import Browser
from pages.activity_page import ActivityPage


URL = "YOUR_ESTIMATE_PAGE_URL"


browser = Browser()

browser.open(URL)

input(
    "\n"
    "1. Login manually\n"
    "2. Open Estimate\n"
    "3. Click Edit\n"
    "4. Press ENTER..."
)

activity = ActivityPage(browser)

activity.open_measurements("79.01.01")

input("\nPress ENTER to close browser...")

browser.close()