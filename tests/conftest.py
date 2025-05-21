
import pytest
from selenium import webdriver



@pytest.fixture()
def driver(request):
    browser = "Chrome"

    print(f"Creating {browser} driver")
    if browser == "Chrome":
        my_driver = webdriver.Chrome()
    elif browser == "Edge":
        my_driver = webdriver.ChromiumEdge()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")

    yield my_driver
    print("Closing {browser} driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
