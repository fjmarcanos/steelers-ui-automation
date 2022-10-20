Feature: Schedule

  Scenario: Upcoming events have buy ticket link
    When the stanzacal widget is loaded
    Then each upcoming event has a buy ticket link and the date is correct

  Scenario: Past events do not have buy ticket link
    When the stanzacal widget is loaded
    Then each past event do not have a buy ticket link

  Scenario: Add to calendar url has correct text
    When the stanzacal widget is loaded
    And the add to calendar button is clicked
    Then the url from the new window contains the text "nfl-steelers"