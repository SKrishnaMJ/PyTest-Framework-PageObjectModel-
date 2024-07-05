from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT,"Shop")

    def gotoShop(self):
        self.driver.find_element(*HomePage.shop).click()
        # We find a connection point between pages, when we click on shop it then goes to shopPage from homePage and thats why
        # we perform the click operation here and then create the shopPage object here and return the shopPage to optimise our testcode
        shopPage = ShopPage(self.driver)
        return shopPage
