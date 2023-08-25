import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from features import global_constants
from features.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __anmelden_popup = (By.XPATH, "//h5/span['Anzeige Filter']")
    __entity_selector_textbox = (By.XPATH, "//input[@id='economic-entity-selection']")
    __entity_select_option = (By.XPATH, "//li[@id='economic-entity-selection-option-0']")
    __entity_select_ee_created = (By.XPATH, "//li[@id='economic-entity-selection-option-0']")
    __entity_select_save_button = (By.XPATH, "//button[@type='submit']")
    __economic_entity_row_cc = (By.XPATH, "//div[@class='MuiDataGrid-windowContainer']//div[2]")
    __ee_menu_link = (By.XPATH, "//div[@class='float-right']/div/div[1]/button[@type='button']")
    __create_ee_link = (By.XPATH, "//span[normalize-space()='Create business entity']")
    __ee_name_field_search=(By.XPATH,"//input[@id='economic-entity-selection']")
    __ee_name_field = (By.XPATH, "//div[@class='row']/div[1]/div/div/input")
    __ee_service_provider_field = (
        By.XPATH, "//form/div[@class='modal-body']/div[2]/div[1]/div/div/div[@role='button']")
    __ee_label_field = (By.XPATH, "//form//div[@class='row']/div[2]/div/div/input")
    __ee_customer_field = (By.XPATH, "//form/div[@class='modal-body']/div[2]/div[2]/div/div/div[@role='button']")
    __ee_owner_field = (
        By.XPATH, "//form/div[@class='modal-body']/div[3]/div[@class='col-md-6']/div/div/div[@role='button']")
    __ee_status_field = (By.XPATH, "//form/div[@class='modal-body']/div[4]/div[1]/div/div/div[@role='button']")
    __ee_status_active_selector = (By.XPATH, "//div[@id='menu-']//ul[@role='listbox']/li[3]")
    __ee_status_serviceprovider_select = (By.XPATH, "//div[@id='menu-']//ul[@role='listbox']/li[1]")
    __ee_status_customer_select = (By.XPATH, "//div[@id='menu-']//ul[@role='listbox']/li[18]")

    __ee_save_button = (By.XPATH, "//div[@role='document']//form//span[.='Save']")
    __ee_cancel_button = (By.XPATH, "//div[@role='document']//form//span[.='Cancel']")
    __ee_create_header = (By.XPATH, "//div[@role='document']//form//span[.='Economic entity']")

    __ee_filter_button = (
    By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root icon icon-exchange MuiIconButton-colorInherit']")

    __ee_new_search_list=(By.XPATH,"//div[@class='MuiDataGrid-windowContainer']//div[2]")

    def verify_login_success(self):
        assert self.driver.find_element(*self.__anmelden_popup).is_displayed(), "Error!Logged in Alert not shown"

    def select_first_time_entity_popup(self):
        self.driver.find_element(*self.__entity_selector_textbox).clear()
        self.driver.find_element(*self.__entity_selector_textbox).click()
        self.driver.find_element(*self.__entity_selector_textbox).send_keys(global_constants.economic_entity_name)
        self.driver.find_element(*self.__entity_select_option).click()
        self.driver.find_element(*self.__entity_select_save_button).click()

    def is_economic_entity_displayed(self) -> bool:
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__economic_entity_row_cc))
        return self.driver.find_element(*self.__economic_entity_row_cc).is_displayed()



    def goto_economic_entity(self):
        wait = WebDriverWait(self.driver, 30)
        # wait.until(ec.presence_of_element_located(self.__economic_entity_row_cc))
        self.driver.find_element(*self.__economic_entity_row_cc).click()

    def is_ee_create_header_displayed(self) -> bool:
        return self.driver.find_element(*self.__ee_create_header).is_displayed()

    def create_economic_entity(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__ee_menu_link))
        self.driver.find_element(*self.__ee_menu_link).click()
        time.sleep(5)
        self.driver.find_element(*self.__create_ee_link).click()
        wait.until(ec.presence_of_element_located(self.__ee_create_header))
        assert self.is_ee_create_header_displayed(), global_constants.header_economic_entity
        self.driver.find_element(*self.__ee_name_field).click()
        self.driver.find_element(*self.__ee_name_field).send_keys(global_constants.new_ee_name)
        self.driver.find_element(*self.__ee_label_field).click()
        self.driver.find_element(*self.__ee_label_field).send_keys(global_constants.new_ee_label)
        self.driver.find_element(*self.__ee_service_provider_field).click()
        wait.until(ec.presence_of_element_located(self.__ee_status_serviceprovider_select))
        self.driver.find_element(*self.__ee_status_serviceprovider_select).click()
        self.driver.find_element(*self.__ee_customer_field).click()
        wait.until(ec.presence_of_element_located(self.__ee_status_customer_select))
        self.driver.find_element(*self.__ee_status_customer_select).click()
        self.page_scroll()
        self.driver.find_element(*self.__ee_save_button).click()

    def open_economic_entity_filter(self):
        self.driver.find_element(*self.__ee_filter_button).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__ee_name_field_search))
        self.driver.find_element(*self.__ee_name_field_search).click()

    def search_economic_entity_created(self):
        self.driver.find_element(*self.__ee_name_field_search).click()
        self.driver.find_element(*self.__ee_name_field_search).send_keys(global_constants.new_ee_name)
        self.driver.find_element(*self.__ee_name_field_search).click()
        self.driver.find_element(*self.__entity_select_option).click()
        self.driver.find_element(*self.__entity_select_save_button).click()

    def check_created_eco_entity_displayed(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__ee_new_search_list))
        # assert self.driver.find_element(*self.__ee_new_search_list).text
        #abc = self.driver.find_element(By.XPATH,
          #                                       "//table[@class='table']/tbody/tr/td[contains(text(),'{}')]".format(                                                     new_contact)).text
        # assert abc == new_contact, global_constants.validation_new_contact_home