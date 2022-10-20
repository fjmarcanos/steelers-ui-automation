from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..constants import DEFAULT_TIMEOUT


# Wait until iFrame is available and switch to it
def wait_until_iframe_is_available_and_switch_to_it(driver, by, value):
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.frame_to_be_available_and_switch_to_it((by, value)))


# Returns the month number based on its abbreviation.
def get_month_number(month_abbr):
    return {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }[month_abbr]


# Switches the current driver to a new window
def switch_to_new_window(driver):
    driver.switch_to.window(driver.window_handles[1])


# Wait until current url contains certain text
def assert_url_contains(driver, expected_url):
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_contains(expected_url))
