from selene import browser
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from resources import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    return selenoid_login, selenoid_pass, selenoid_url


@pytest.fixture(scope='session')
def open_browser(load_env):
    selenoid_login, selenoid_pass, selenoid_url = load_env
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )



    browser.config.driver = driver

    yield driver

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

@pytest.fixture(scope='session')
def open_demoqa(open_browser):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.driver.fullscreen_window()
