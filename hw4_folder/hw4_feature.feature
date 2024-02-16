# TracyArispe at 2/4/2024

Feature: Target.com user features

  
  Scenario: Verify item added to cart on Target.com
    Given Open Target main page
    When Type search word yankee candles into textbox
    When Click the search icon
    When Click Add to cart button
    When Click on Pick Up button
    When Click Side Panel Add to Cart button
    When click on View cart & check out
    Then Verify 22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle message is shown

    Scenario: Verify 5 benefit boxes are shown on Target.com circle page
    Given Open Target circle page
    Then Verify 5 benefit boxes are shown

    Scenario: Verify Target.com help UI
    Given Open Target help UI page
    Then Verify Target Help text is shown
      Then Verify 7 link boxes are shown
      Then Verify 2 information boxes are shown
      Then Verify Browse all Help pages text is visible


