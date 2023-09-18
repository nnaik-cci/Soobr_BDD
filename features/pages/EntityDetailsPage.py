import contextvars
import datetime
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from features import global_constants
from features.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec


class EntityDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __cc_economic_entity_row = (By.XPATH, "//div[normalize-space()='Creative Capsule Tower']")
    __tab_cleaning_areas = (By.XPATH, "//span[normalize-space()='Cleaning areas']")
    __tab_tour_activities = (By.XPATH, "//span[normalize-space()='Tour activities']")

    __tab_building_overview = (By.XPATH, "//span[normalize-space()='Building overview']")
    __tab_tours = (By.XPATH, "//span[normalize-space()='Tours']")
    __tour_activities_table = (By.XPATH, "")
    __tower_expand_link = (By.XPATH, "//div[@class='building-table']/div[5]//div[1]//div[4]//span[1]//span["
                                     "@class='MuiIconButton-label']//input")
    __cleaning_area_1 = (By.XPATH, "//div[@id='cleaning-area-48334']")
    # __cleaning_area_2 = (By.XPATH, "//div[@id='cleaning-area-48336']")
    __tour_info_tab = (By.XPATH, "//span[normalize-space()='Tour Information']")
    __cleaning_area1_name = (By.XPATH, "// div[ @ id = 'cleaning-area-48334'] // span[contains(text(), 'Floor 5-3 "
                                       "Tour 2')]")
    __cleaning_area_1_element = (By.XPATH, "// div[ @ id = 'cleaning-area-48334']")
    __cleaning_area1_polygon = (By.XPATH, "//*[name()='svg'][1]/*[name()='g'][@id='cleaning-area-g-48334']")
    # __area_3F_table = (By.XPATH, "//div[@class='building-table-cleaning-areas-body row']/div[1]/div")
    __area_3F_row = (By.XPATH, "//div[@class='cleaning-area-lane align-items-center  row']")

    def verify_ee_page_navigation(self):
        assert self.driver.current_url == global_constants.cleaning_areas_url, global_constants.validation_incorrect_url
        assert self.driver.find_element(
            *self.__tab_cleaning_areas).is_displayed(), "Error! Cleaning areas tab not displayed!"

    def navigate_to_tour_activities_tab(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__tab_tour_activities))
        self.driver.find_element(*self.__tab_tour_activities).click()
        assert self.driver.current_url == global_constants.tour_activities_url, global_constants.validation_incorrect_url

    def go_to_tower_area(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__tower_expand_link))
        self.driver.find_element(*self.__tower_expand_link).click()

    def check_planned_area(self):
        # time.sleep(5)
        results = self.driver.find_elements(By.XPATH,
                                            "//div[@class='cleaning-area-lane align-items-center  row']")
        time.sleep(2)
        xyz = []
        newList = []
        for result in results:
            row = self.driver.find_elements(By.XPATH,
                                            "//div[@class='cleaning-area-lane align-items-center  row']")
            time.sleep(2)
            if 'Min.' in result.text:
                xyz.append(result.text)

        for i in xyz:
            if len(xyz) <= 1:
                newList.append(i)
            else:
                newList.append(i.split(','))
                time.sleep(3)
        tour_name = newList[0]
        final_area = str(tour_name).split('\\n')
        # return final_area[4]
        area_name = final_area[0]
        t1 = area_name.replace("[", "")
        final_tour_name = t1.replace("'", "")
        # time.sleep(5)
        test1 = "//div[@class='cleaning-area-lane align-items-center  row']/div/span[contains(text(),'{}')]".format(
            final_tour_name)
        test = self.driver.find_element(By.XPATH, test1).text
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, test1)
        a.scroll_to_element(m)
        a.move_to_element(m).perform()
        # time.sleep(5)
        '''selected_area = self.driver.find_element(By.XPATH,
                                                 "//*[@id='FloorPlanMap']//*[local-name()='g' and @id='cleaning-area-g-48334']")'''
        elem = self.driver.find_element(By.XPATH,
                                        "//*[@id='FloorPlanMap']//*[local-name()='g' and @id='cleaning-area-g-48343']//*[local-name()='polygon']")
        test11 = elem.get_attribute("fill")
        time.sleep(3)
        # color = getattr(selected_area, 'fill')
        assert test11 == '#8a8a8a', "Wrong color"

    def check_running_status(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__tour_info_tab))
        self.driver.find_element(*self.__tour_info_tab).click()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, "//td[normalize-space()='Floor 5-3 Tour 2']")
        info_rows = self.driver.find_elements(By.XPATH,
                                              "//table[@class='table table-hover']/tbody/tr")
        xyz = []
        info_row = []
        for result1 in info_rows:
            row = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr")
            if 'Floor 5-3 Tour 2' in result1.text:
                time.sleep(3)
                xyz.append(result1.text)
        time.sleep(3)
        info_row = str(xyz).split(' ')
        status_a = info_row[3]
        status_b = info_row[4]
        time.sleep(5)
        if status_a != 'Not' and status_b == 'Running':
            assert True
        else:
            assert False
        '''app input and then switch'''
        # go to tour activities sub tab under tour activities
        wait.until(ec.presence_of_element_located(self.__tab_tour_activities))
        self.driver.find_element(*self.__tab_tour_activities).click()
        test = self.driver.find_element(By.XPATH,
                                        "//div[@class='mt-3 row']/div[@class='col']/ul//span[.='Tour activities']")
        test.click()
        # assert self.driver.current_url == global_constants.tour_activities_url, global_constants.validation_incorrect_url
        green_elem = self.driver.find_element(By.XPATH,
                                              "//*[@id='FloorPlanMap']//*[local-name()='g' and @id='cleaning-area-g-48335']//*[local-name()='polygon']")
        check = green_elem.get_attribute("fill")
        time.sleep(3)
        # color = getattr(selected_area, 'fill')
        assert check == '#38cb89', "Wrong color"
        green_elem.click()
        # verify that area analysis window opens
        # wait.until(ec.presence_of_element_located(By.XPATH, "//span[normalize-space()='Area analysis']"))
        assert self.driver.find_element(By.XPATH,
                                        "//span[normalize-space()='Area analysis']").text == "Area analysis", "Area analysis window not opened!"
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Completed']").click()
        time.sleep(3)
        # check that first entry has the cleaned floor

        wait.until((ec.presence_of_element_located(
            (By.XPATH, "//div[@class='cleaning-area-planning-dialog-scroll-list planning-result']/div[1]"))))
        # get all values of that row
        completed_row_text = []
        completed_row_text = self.driver.find_element(By.XPATH,
                                                      "//div[@class='cleaning-area-planning-dialog-scroll-list planning-result']/div[1]").text
        time.sleep(3)
        completed_result = completed_row_text.split("\n")
        comp_tour = completed_result[0]
        comp_date = completed_result[0]
        assert comp_tour == 'Floor 5-3 Tour 2', "Incorrect cleaned tour name!"
        current_date = datetime.date.today()
        assert comp_date == current_date,"Cleaned date correct!"
        #self.driver.find_element(By.XPATH,"//i[@id='cleaning-5-info']  info icon")
        # if info icon exists hover over it

        p = ActionChains(self.driver)
        q = self.driver.find_element(By.XPATH,"//i[@id='cleaning-5-info']  info icon")
        p.move_to_element(q).perform()
        time.sleep(5)

    def hover_to_cleaning_area(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__cleaning_area_1))
        # wait.until(ec.presence_of_element_located(self.__cleaning_area_2))
        a = ActionChains(self.driver)
        m = self.driver.find_element(*self.__cleaning_area_1)
        # y = self.driver.find_element(*self.__cleaning_area_2)
        a.move_to_element(m).perform()
        time.sleep(5)
        # a.move_to_element(y).perform()
        # time.sleep(5)

    def capture_area_to_clean(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__cleaning_area_1_element))
        abc = self.driver.find_element(*self.__cleaning_area_1_element).text
        time.sleep(5)

    def check_if_area_cleaned(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.test))

    def goto_tour_info_tab(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(self.__tour_info_tab))
        self.driver.find_element(*self.__tour_info_tab).click()
