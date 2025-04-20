import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="function")
def browser_init(request):
    service = Service()
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service)
    else:
        raise pytest.UsageError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.quit()