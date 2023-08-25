import time

from behave import *
from selenium import webdriver

from features import global_constants
from features.pages.DashboardPage import DashboardPage


@when(u'user clicks on Create Economic entity button')
def user_clicks_create_eco_entity(context):
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.is_economic_entity_displayed()
    dashboard_page.page_scroll()
    time.sleep(5)
    dashboard_page.create_economic_entity()


@then(u'Economic entity should be successfully created')
def entity_creation_success_check(context):
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.open_economic_entity_filter()
    dashboard_page.search_economic_entity_created()
    dashboard_page.page_scroll()

@then(u'Economic entity should be displayed')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.check_created_eco_entity_displayed()


@given(u'Soobr dashboard is open')
def soobr_dashboard_is_open(context):
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.verify_login_success()
    dashboard_page.select_first_time_entity_popup()
    time.sleep(5)

@when(u'economic entity is selected')
def step_impl(context):
    print("success ")


@then(u'User should be displayed details')
def step_impl(context):
    print("success")

@given(u'Economic entity is created and open')
def step_impl(context):
    pass


@when(u'User clicks on Building overview tab')
def step_impl(context):
    pass


@when(u'User clicks on Create new Building button')
def step_impl(context):
    pass


@when(u'User enters and saves Building data')
def step_impl(context):
    pass


@when(u'User uploads building plan')
def step_impl(context):
    pass


@then(u'new Building should be created under Economic entity')
def step_impl(context):
    pass

@then(u'new Building should be created under Building overview tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then new Building should be created under Building overview tab')


@when(u'User completes upload building plan steps')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User completes upload building plan steps')
