Feature: Economic entity

#Background: Soobr admin is logged in
@xyz
  Scenario: To verify successful creation of economic entity
    Given Admin is logged in to Soobr
    And   Soobr dashboard is open
    When  user clicks on Create Economic entity button
    Then  Economic entity should be successfully created
    Then  Economic entity should be displayed

  Scenario: To create building under Economic entity
    Given Economic entity is created and open
    When  User clicks on Building overview tab
    And   User clicks on Create new Building button
    And   User enters and saves Building data
    Then  new Building should be created under Building overview tab
    When  User completes upload building plan steps

  

