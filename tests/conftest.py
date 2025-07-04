import pytest
from selenium import webdriver
import os
from datetime import datetime


# Pytest fixture to set up the Chrome browser before each test,
# and close it after test ends. Takes screenshot on failure.   
@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.entrata.com")
    driver.maximize_window()

    yield driver

    # Capture screenshot on failure
    if request.node.rep_call.failed:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = f"{screenshot_dir}/{request.node.name}_{now}.png"
        driver.save_screenshot(screenshot_path)

    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    #Hook for capturing the result of each test (needed for screenshot logic)
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
