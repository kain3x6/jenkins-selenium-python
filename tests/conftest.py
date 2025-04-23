import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="function")
def browser_init(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.binary_location = "/usr/bin/google-chrome"  # Путь к установленному Chrome

        driver = webdriver.Chrome
        (
            service=ChromeService(executable_path="/usr/bin/chromedriver"),  # <-- укажи путь
            options=options
        )


    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise pytest.UsageError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()
