import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="function")
def browser_init(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # Настройка ChromeOptions для работы в headless-режиме в контейнере
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Указание на URL для подключения к Selenium Grid в контейнере
        # Внутри Docker контейнера с Selenium этот адрес будет использоваться для связи с браузером
        driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",  # URL к Selenium Server внутри контейнера(где selenium,4444 - это название и порт внутри docker-compose)
            options=options
        )

    else:
        raise pytest.UsageError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
