import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.pages.BasePage import BasePage
from features.pages.DashboardPage import DashboardPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __username_field = (By.XPATH, "//input[@type='text']")
    __password_field = (By.XPATH, "//input[@type='password']")
    __login_button = (By.XPATH, "//span[normalize-space()='Anmelden']")

    def perform_login(self, username, password):
        wait = WebDriverWait(self.driver, 50)
        wait.until(ec.presence_of_element_located(self.__username_field))
        self.driver.find_element(*self.__username_field).send_keys(username)
        wait.until(ec.presence_of_element_located(self.__password_field))
        self.driver.find_element(*self.__password_field).send_keys(password)
        wait.until(ec.presence_of_element_located(self.__login_button))
        self.driver.find_element(*self.__login_button).click()

    def perform_invalidlogin(self, username, password):
        self.driver.find_element(*self.__username_field).send_keys(username)
        self.driver.find_element(*self.__password_field).send_keys(password)
        time.sleep(5)  # to be removed
        self.driver.find_element(*self.__login_button).click()
        time.sleep(10)  # to be removed

    def verify_login_page_is_open(self):
        assert self.driver.current_url == "http://qa-soobr.creativecapsule.ccigoa:8080/login", "You are on wrong page!"
        assert self.driver.find_element(By.XPATH, "//input[@type='text']"), "Login fields missing!"
