import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# We define driver here so that ot can be used globally throughout this class across all methods later
driver = None


# This function helps set command line variables, here we have defined browser_name
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # This global keyword allows the driver to be used anywhere within this class
    global driver
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

# This method gets called whenever there is a failure in a test and attaches the screenshot of the step failed to the report.html
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)