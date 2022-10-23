import re
from datetime import datetime
from pytest_bdd import scenarios, when, then, parsers
from .utils.driver_utils import *
from .pages.schedule_widget import ScheduleWidget

scenarios('../features/schedule.feature')


# When Steps
@when('the stanzacal widget is loaded')
def assert_widget_is_present(driver):
    wait_until_iframe_is_available_and_switch_to_it(driver, *ScheduleWidget.STANZACAL_WIDGET_IFRAME)


@when('the add to calendar button is clicked')
def click_add_to_calendar_button(driver):
    ScheduleWidget(driver).click_add_to_calendar_button()
    switch_to_new_window(driver)


# Then Steps
@then('each upcoming event has a buy ticket link and the date is correct')
def assert_ticket_link_exists(driver):
    future_events_tiles = ScheduleWidget(driver).get_future_events_tiles()

    past_event_month = 0
    current_year = datetime.today().year
    for tile in future_events_tiles:
        # Check if the event has a date. If not, it should not have a tickets link
        event_description = tile.find_element(*ScheduleWidget.EVENT_TILE_DESCRIPTION).text
        if event_description is not None and '(Date/time subject to change)' in event_description:
            continue

        # Assert ticket link exists
        ticket_link = tile.find_element(*ScheduleWidget.EVENT_TILE_TICKET_LINK).get_attribute('href')
        assert ticket_link

        # Assert link date is correct
        date_regex = r"(\d{2}-\d{2}-\d{4})"
        url_date = re.search(date_regex, ticket_link).group(1)
        splitted_url_date = url_date.split('-')
        url_month = int(splitted_url_date[0])
        url_day = int(splitted_url_date[1])
        url_year = int(splitted_url_date[2])

        event_date = tile.find_element(*ScheduleWidget.EVENT_TILE_DATE).text
        if event_date.lower() == 'today':
            event_month = datetime.today().month
            event_day = datetime.today().day
        else:
            event_month = get_month_number(event_date[5:8].lower())
            event_day = int(event_date[9:])

        # Assuming the event list is sorted by date, if a previous month is found,
        # then that means that it is from the next year
        if past_event_month > event_month:
            current_year = current_year + 1

        assert url_month == event_month
        assert url_day == event_day
        assert url_year == current_year

        past_event_month = event_month
    driver.quit()


@then('each past event do not have a buy ticket link')
def assert_ticket_link_not_exists(driver):
    past_events_tiles = ScheduleWidget(driver).get_past_events_tiles()
    for tile in past_events_tiles:
        ticket_link = tile.find_elements(*ScheduleWidget.EVENT_TILE_TICKET_LINK)
        assert not ticket_link
    driver.quit()


@then(parsers.parse('the url from the new window contains the text "{text}"'))
def assert_url_contains_text(driver, text):
    assert_url_contains(driver, text)
    driver.quit()
