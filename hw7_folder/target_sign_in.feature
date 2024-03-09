# Created by Tracy Arispe at 3/4/2024

  Feature: Target.com sign-in features

  Scenario: User can open the sign-in form on Target.com
    Given Open Target main page
    When Click on sign in icon
    When Click on Account sign in icon
    Then Verify By signing in, you agree to the following: message displays accurately
