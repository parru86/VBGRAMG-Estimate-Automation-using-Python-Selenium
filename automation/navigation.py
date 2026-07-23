from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def open_draft_estimate(driver, wait):

    print("Dashboard Opened")

    time.sleep(5)   # Dashboard पूरी तरह लोड होने दें

    try:
        estimates = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/section[2]/div/div[2]/div/div[2]/div/div/div/div/div[3]/ul/li/a")
            )
        )

        print("Estimates Found")

        driver.execute_script("arguments[0].scrollIntoView(true);", estimates)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", estimates)

        print("Estimates Clicked")

    except Exception as e:
        print("Estimates Error:", e)
        return

    time.sleep(2)

    try:
        draft = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/section[2]/div/div[2]/div/div[2]/div/div/div/div/div[3]/ul/li/ul/li/ul/li[2]/a")
            )
        )

        print("Draft Found")

        driver.execute_script("arguments[0].click();", draft)

        print("Draft Estimate Opened")

    except Exception as e:
        print("Draft Error:", e)
        
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def search_estimate(driver, wait, estimate_no):

    # Search Box
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "04873"))
    )

    search_box.clear()
    search_box.send_keys(estimate_no)

    print("Estimate Number Entered")

    # Search Button
    search_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/section[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/section/div/button")
        )
    )

    driver.execute_script("arguments[0].click();", search_btn)

    print("Search Button Clicked")

    time.sleep(3)
    
    
    