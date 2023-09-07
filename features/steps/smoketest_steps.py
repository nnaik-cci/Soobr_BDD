import time
from behave import *
from features import global_constants
from features.pages.DashboardPage import DashboardPage
from features.pages.EntityDetailsPage import EntityDetailsPage
from features.pages.LoginPage import LoginPage


@given(u'Admin is logged in to Soobr')
def step_impl(context):
    login_page = LoginPage(context.driver)
    dashboard_page = DashboardPage(context.driver)
    login_page.perform_login(global_constants.username_admin_stage, global_constants.password_admin_stage)
    dashboard_page.verify_loggedin_dashboard()


@given(u'I Select and navigate to Economic entity from dashboard')
def navigate_to_ee_detail_page(context):
    dashboard_page = DashboardPage(context.driver)
    entity_details_page= EntityDetailsPage(context.driver)
    dashboard_page.page_scroll()
    dashboard_page.open_cc_economic_entity()
    time.sleep(5)
    entity_details_page.verify_ee_page_navigation()



@given(u'I click Tour activities tab under Tour activities')
def click_tour_activities_tab(context):
    entity_details_page= EntityDetailsPage(context.driver)
    entity_details_page.navigate_to_tour_activities_tab()


@when(u'I expand rows on building floor entry')
def step_impl(context):
    pass


@then(u'Planned tour should be present  and captured (not 0 mins)')
def step_impl(context):
    pass


@when(u'I open Soobr app on tablet')
def step_impl(context):
    pass


@when(u'I login as a cleaning staff')
def step_impl(context):
    pass


@when(u'I find required planned tour saved in web')
def step_impl(context):
    pass


@when(u'verify that planned tour has red color circle')
def step_impl(context):
    pass


@when(u'I tap on Start tour button')
def step_impl(context):
    pass


@then(u'Tour information tab in cockpit should have started status for the required tour')
def step_impl(context):
    pass


@when(u'I select floor and area marked in red on floor plan')
def step_impl(context):
    pass
