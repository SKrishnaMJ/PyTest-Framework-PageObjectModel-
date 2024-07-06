from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT,"Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radioBtn = (By.ID, "inlineRadio2")
    submit = (By.XPATH, "//input[@type='submit']")
    succesMsg = (By.CLASS_NAME, "alert-success")
    dropdown = (By.ID, "exampleFormControlSelect1")

    def gotoShop(self):
        self.driver.find_element(*HomePage.shop).click()
        # We find a connection point between pages, when we click on shop it then goes to shopPage from homePage and thats why
        # we perform the click operation here and then create the shopPage object here and return the shopPage to optimise our testcode
        shopPage = ShopPage(self.driver)
        return shopPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getRadioBtn(self):
        return self.driver.find_element(*HomePage.radioBtn)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.succesMsg)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)


