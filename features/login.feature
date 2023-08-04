Feature: Soobr Admin Login
  @abc
  Scenario: To verify successful login to Soobr cockpit
    Given Soobr cockpit login page is open
    When  Valid login credentials are provided
    Then  User should be successfully logged in


  Scenario: To verify unsuccessful login to Soobr cockpit
    Given Soobr cockpit login page is open
    When  invalid login credentials are provided
    Then  user should not be logged in


  Scenario: To verify logged in dashboard of admin cockpit
    Given Soobr admin is logged in
    And   Soobr dashboard is open
    When  economic entity is selected
    Then  User should be displayed details
