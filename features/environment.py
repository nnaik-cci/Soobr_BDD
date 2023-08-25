from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    browsername = ConfigReader.read_configuration("basic info", "browser")
    if browsername.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browsername.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browsername.__eq__("edge"):
        context.driver = webdriver.Edge()
    context.driver.maximize_window()
    test = ConfigReader.read_configuration("basic info", "url")
    print(test)
    context.driver.get(test)


def after_scenario(context, driver):
    context.driver.quit()