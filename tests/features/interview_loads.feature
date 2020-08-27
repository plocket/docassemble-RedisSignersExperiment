Feature: Interview loads

Just want to make sure this interview loads
before moving on to more complicated tests.

Scenario: Open the first page
    Given I start the interview
    When I wait 1 second
    Then an element should have the id "#daMainQuestion"
