from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver

    checkbox = (By.CSS_SELECTOR, ".checkbox")
    typeBox = (By.ID, 'country')
    country = (By.LINK_TEXT, 'India')
    purchaseBtn = (By.CSS_SELECTOR, "[value='Purchase']")
    msg = (By.CSS_SELECTOR, ".alert")

    def getCheckbox(self):
        return self.driver.find_element(*PurchasePage.checkbox)

    def typeCountry(self):
        return self.driver.find_element(*PurchasePage.typeBox)

    def selectCountry(self):
        return self.driver.find_element(*PurchasePage.country)

    def getPurchaseBtn(self):
        return self.driver.find_element(*PurchasePage.purchaseBtn)

    def getMessage(self):
        return self.driver.find_element(*PurchasePage.msg)


