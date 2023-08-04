from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("http://qa-soobr.creativecapsule.ccigoa:8080/")


def after_scenario(context, driver):
    context.driver.quit()
