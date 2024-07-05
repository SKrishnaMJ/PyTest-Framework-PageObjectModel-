import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_e2e(self):

        homePage = HomePage(self.driver)

        homePage.gotoShop().click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
        time.sleep(3)
        items = self.driver.find_elements(By.CSS_SELECTOR, "app-card")

        for item in items:
            itemName = item.find_element(By.CSS_SELECTOR, "div h4").text
            if itemName == "Blackberry":
                item.find_element(By.CSS_SELECTOR, "div button").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()

        self.driver.find_element(By.ID, 'country').send_keys("ind")
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.suggestions ul li a')))
        self.driver.find_element(By.LINK_TEXT, 'India').click()
        self.driver.find_element(By.CSS_SELECTOR, "[value='Purchase']").click()
        successMsg = self.driver.find_element(By.CSS_SELECTOR, ".alert").text
        assert "Success! Thank you" in successMsg
