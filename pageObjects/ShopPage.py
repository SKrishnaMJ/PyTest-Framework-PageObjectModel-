from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    items = (By.CSS_SELECTOR, "app-card")
    itenName = (By.CSS_SELECTOR, "div h4")
    checkoutBtn = (By.CSS_SELECTOR, ".btn-primary")

    def getItems(self):
        return self.driver.find_elements(*ShopPage.items)

    def getItemName(self):
        return self.driver.find_elements(*ShopPage.itenName)

    def getCheckoutBtn(self):
        return self.driver.find_element(*ShopPage.checkoutBtn)
