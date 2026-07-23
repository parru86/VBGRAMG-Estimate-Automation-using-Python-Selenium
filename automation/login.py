from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def do_login(driver, wait, userid, password):

    driver.get("https://secure.dord.gov.in/securev2/")

    # LOGIN HERE
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/section/div/div/div/div/a")
        )
    ).click()

    # User ID
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/div/form/div/div/div/div/div[2]/input[2]")
        )
    ).send_keys(userid)

    # Password
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/form/div/div/div/div/div[3]/input[2]"
    ).send_keys(password)

    print("CAPTCHA भरें और Login करें...")
    input("Login होने के बाद Enter दबाएँ...")