from playwright.sync_api import Page, Playwright, expect
import time
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    
@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")  #--browser_name firefox

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless= False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless= False)

    context = browser.new_context()
    page = context.new_page()
    
    yield page

    context.close()
    browser.close()