from automation.browser import Browser

from pages.appendix_page import AppendixPage

browser = Browser()

browser.open("https://secure.dord.gov.in/securev2/")

input("""
Manual Steps

1.Login

2.Open Draft Estimate

3.Select Estimate

4.Click Edit

5.When Estimate opens

Press ENTER...
""")

page = AppendixPage(browser)

page.create_appendix("dabari")

print("Appendix Completed")

input()

browser.close()