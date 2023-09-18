Feature: Economic entity

#Background: Soobr admin is logged in

  Scenario: To verify cleaning flow
    Given Admin is logged in to Soobr
    And I Select and navigate to Economic entity from dashboard
    And I click Tour activities tab under Tour activities
    When I expand rows on building floor entry
    Then Planned tour should be present and captured
    #When I open Soobr app on tablet
   # And I login as a cleaning staff
    #And I find required planned tour saved in web
    #And verify that planned tour has red color circle
   # And I tap on Start tour button
    Then Tour information tab in cockpit should have running status for the required tour
   # When I open Soobr app on tablet
    #And I select floor and area marked in red on floor plan
    #And I clean the area and mark as "Area is clean"
   # Then  area color should change to green in app
    #And  area cleaned should be verified in cockpit

