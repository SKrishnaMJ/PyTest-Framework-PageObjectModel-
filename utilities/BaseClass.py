import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# This class is inherited to all the Test classes so that we can get the fixtures and code looks
# more clean and optimised
@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyElePresence(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, locator)))