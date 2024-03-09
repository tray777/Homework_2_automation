# Created by Tracy Arispe at 3/5/2024
Feature: Target.com add to cart features

  Scenario: Verify item added to cart on Target.com
    Given Open Target main page
    When Type search word yankee candles into textbox
    When Click the search icon
    When Click Add to cart button
    When Click on Pick Up button
    When Click Side Panel Add to Cart button
    When click on View cart & check out
    Then Verify 22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle message is shown
