# TracyArispe at 2/4/2024

Feature: Target.com user features


  Scenario: Verify user cart is empty on Target.com
    Given Open Target main page
    When Click on cart icon
    Then Verify Your cart is empty text displays


  Scenario: User can search for coffee on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee are shown
    Then Page URL has search term coffee


