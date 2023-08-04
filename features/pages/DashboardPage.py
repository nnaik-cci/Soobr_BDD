import time

from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    __anmelden_popup = (By.XPATH, "//h5/span['Anzeige Filter']")

    ''' def perform_login(self, username, password):
        self.driver.find_element(*self.__username_field).send_keys(username)
        self.driver.find_element(*self.__password_field).send_keys(password)
        time.sleep(5)  # to be removed
        self.driver.find_element(*self.__login_button).click()
        time.sleep(5)  # to be removed
        '''
    def verify_login_success(self):
        assert self.driver.find_element(*self.__anmelden_popup).is_displayed(), "Error!Logged in Alert not shown"
