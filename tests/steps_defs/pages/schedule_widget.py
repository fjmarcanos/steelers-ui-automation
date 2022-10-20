from selenium.webdriver.common.by import By


class ScheduleWidget:

    def __init__(self, driver):
        self.driver = driver

    # List of elements (locator strategy, value)
    STANZACAL_WIDGET_IFRAME = (By.NAME, 'sdk-stanzacal')
    EVENTS_LIST = (By.ID, 'tile-list')
    FUTURE_EVENT_TILE = (By.CSS_SELECTOR, ".event-tile.future")
    PAST_EVENT_TILE = (By.CSS_SELECTOR, ".event-tile.past")
    EVENT_TILE_TICKET_LINK = (By.CSS_SELECTOR, ".tile-link.ticket")
    EVENT_TILE_DESCRIPTION = (By.CLASS_NAME, "tile-data-description")
    EVENT_TILE_DATE = (By.CLASS_NAME, "tile-data-date")
    ADD_TO_CALENDAR_BUTTON = (By.XPATH, "//span[contains(.,'ADD TO CALENDAR')]")

    # Elements getters

    def get_future_events_tiles(self):
        events_list = self.driver.find_element(*self.EVENTS_LIST)
        return events_list.find_elements(*self.FUTURE_EVENT_TILE)

    def get_past_events_tiles(self):
        events_list = self.driver.find_element(*self.EVENTS_LIST)
        return events_list.find_elements(*self.PAST_EVENT_TILE)

    # Elements actions

    def click_add_to_calendar_button(self):
        self.driver.find_element(*self.ADD_TO_CALENDAR_BUTTON).click()
