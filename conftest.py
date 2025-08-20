import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import attach_utils


@pytest.fixture(scope="function", autouse=True)
def browser_options():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True,
            "logName": "browser.log"
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url='https://demoqa.com'

    yield browser

    attach_utils.add_html(browser)
    attach_utils.add_screenshot(browser)
    attach_utils.add_logs(browser)
    attach_utils.add_video(browser)

    browser.quit()