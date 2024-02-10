# TracyArispe at 2/4/2024
Feature: Target.com user features


  Scenario: Verify user cart is empty on Target.com
    Given Open Target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: User can open the sign-in form on Target.com
    Given Open Target main page
    When Click on sign in icon
    When Click on Account sign in icon
    Then Verify “By signing in, you agree to the following:” message is shown


  Scenario: Verify item added to cart on Target.com
    Given Open Target main page
    When Type search word 'yankee candles' into textbox
    When Click the search icon
    When Click Add to cart button
    When Click on Pick Up button
    When Click Side Panel Add to Cart button
    When click on View cart & check out
    Then Verify “22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle” message is shown