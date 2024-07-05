from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.CSS_SELECTOR, ".btn-success")

    def checkoutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkout)