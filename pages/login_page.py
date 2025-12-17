from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    success_msg = (By.ID, "flash")

    def open_url(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(user)

        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(pwd)

        self.driver.find_element(*self.login_btn).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        ).text
