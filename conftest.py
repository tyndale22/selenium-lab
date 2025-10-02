import base64
import pytest
from pytest_html import extras
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_select(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "safari":
        driver = webdriver.Safari()

    driver.implicitly_wait(4)
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.maximize_window()
    yield driver
    driver.close()


# Hook: Attach screenshot to HTML report if test fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshot for test failures during execution phase
    if report.when == "call" and report.failed:
        web_driver = item.funcargs.get("browser_select")
        if web_driver:
            # Take screenshot as PNG (in memory)
            screenshot_png = web_driver.get_screenshot_as_png()

            # Encode as base64 for embedding
            encoded_image = base64.b64encode(screenshot_png).decode("utf-8")

            # HTML <img> tag with base64 image
            html_image = f'<img src="data:image/png;base64,{encoded_image}" alt="screenshot" style="width:600px;height:auto;" />'

            # Attach image to report
            report.extra = getattr(report, "extra", [])
            report.extra.append(extras.html(html_image))