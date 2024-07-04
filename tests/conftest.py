import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()