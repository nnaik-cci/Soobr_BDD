Feature: Economic entity
  Scenario: To verify successful creation of economic entity
    Given Soobr admin is logged in
    And   Soobr dashboard is open
    When  click on Create Economic entity button
    Then  Economic entity should be successfully created
    Then  Economic entity should be displayed

