Feature: MakeMyTrip Homepage
  Scenario: Verify user is able to login into the application
    Given launch chrome browser
    When user verify the Title of the Page "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"

@cal
  Scenario: Verify user can book a One Way ticket for future date
    Given launch chrome browser
    When click on departure date
    And enter the date "9 August 2025"


@cal2
  Scenario Outline: Verify user can book a One Way ticket for multiple future date
    Given launch chrome browser
    When click on departure date
    And enter the date "<date>"
    Examples:
        |date|
        |8 August 2025|
        |12 September 2024|




