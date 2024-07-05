from selenium.webdriver.common.by import By

from pageObjects.PurchasePage import PurchasePage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.CSS_SELECTOR, ".btn-success")

    def checkoutBtn(self):
        self.driver.find_element(*CheckOutPage.checkout).click()
        purchasePage = PurchasePage(self.driver)
        return purchasePage
