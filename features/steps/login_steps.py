import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features import global_constants
from features.pages.DashboardPage import DashboardPage
from features.pages.LoginPage import LoginPage


@given(u'Soobr cockpit login page is open')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.verify_login_page_is_open()


@when(u'valid login credentials are provided')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.perform_login(global_constants.uername_admin_qa, global_constants.password_admin_qa)


@when(u'invalid login credentials are provided')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.perform_invalidlogin("neha.aik", "abcd")


@then(u'user should be successfully logged in')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.verify_login_success()


@then(u'user should not be logged in')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[ @class ='Toastify__toast-container "
                                                 "Toastify__toast-container--top-left toastify-container'] // div[1] "
                                                 "// div["
                                                 "1]").is_displayed(), "check code!"


@given(u'Soobr admin is logged in')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.perform_login(global_constants.username_admin_qa, global_constants.password_admin_qa)
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.verify_login_success()



