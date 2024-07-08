import pytest
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomepageData
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):
    def test_FormSubmission(self, getData):

        logger = self.getLogger()

        homePage = HomePage(self.driver)
        logger.info("The firstname used is " +getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckbox().click()

        # Select class to handle static dropdown
        self.selectByVisibleText(homePage.getDropdown(), getData["gender"])

        homePage.getRadioBtn().click()

        # Xpath Syntax - //tagname[@attribute_name='value'] --> //input[@type='submit']
        homePage.getSubmitBtn().click()
        message = homePage.getMessage().text
        logger.info("The message is" +message)

        # to pass or fail tests we use assert class
        assert "Success" in message
        # refresh is used here because we are invoking the website only once through our fxiture whose scope is class and hence
        # with mutliple datasets it starts concatinating to the previous data set on the from and thats why at the end we refresh the driver
        # so that it starts with the next data set afresh
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.data)
    def getData(self, request):
        return request.param
