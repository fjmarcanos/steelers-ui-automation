import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.steps_defs.constants import BASE_URL, DEFAULT_TIMEOUT


# Driver setup
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(DEFAULT_TIMEOUT)
    driver.get(BASE_URL)
    driver.maximize_window()
    return driver
