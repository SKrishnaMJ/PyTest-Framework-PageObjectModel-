import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# This function helps set command line variables, here we have defined browser_name
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=chromeOptions)
    elif browser_name == "firefox":
    #     firefox invocation
        pass
    elif browser_name == "ie":
    #     IE invocation
        pass

    driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()