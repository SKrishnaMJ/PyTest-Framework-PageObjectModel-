import pytest
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):
    def test_FormSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData[0])
        homePage.getEmail().send_keys(getData[1])
        homePage.getPassword().send_keys(getData[2])
        homePage.getCheckbox().click()

        # Select class to handle static dropdown
        self.selectByVisibleText(homePage.getDropdown(), getData[3])

        homePage.getRadioBtn().click()

        # Xpath Syntax - //tagname[@attribute_name='value'] --> //input[@type='submit']
        homePage.getSubmitBtn().click()
        message = homePage.getMessage().text
        print(message)

        # to pass or fail tests we use assert class
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=[("Sai Krishna", "saik@gmail.com", "12345", "Male"), ("Ritika G", "rg001@gmail.com", "87654", "Female")])
    def getData(self, request):
        return request.param
