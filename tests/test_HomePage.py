from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):
    def test_FormSubmission(self):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Sai Krishna M J")
        homePage.getEmail().send_keys("saik@gmail.com")
        homePage.getPassword().send_keys("12345")
        homePage.getCheckbox().click()

        # Select class to handle static dropdown
        self.selectByVisibleText(homePage.getDropdown(), "Female")

        homePage.getRadioBtn().click()

        # Xpath Syntax - //tagname[@attribute_name='value'] --> //input[@type='submit']
        homePage.getSubmitBtn().click()
        message = homePage.getMessage().text
        print(message)

        # to pass or fail tests we use assert class
        assert "Success" in message
