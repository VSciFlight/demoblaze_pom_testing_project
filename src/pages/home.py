from src import utils as u
from src.locators.locators_index import HomepageLocator


class HomePage:

    def __init__(self, driver):
        self.driver = driver

#######################################################################################################################################################################

################################################################ Slideshow #################################################################################################

    def click_right_arrow_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_Right_Arrow'])).click()

    def click_left_arrow_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_Left_Arrow'])).click()

    def click_leftslide_indicator(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_LeftSlide_indicator'])).click()

    def click_midleslide_indicator(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_MiddleSlide_indicator'])).click()

    def click_rightslide_indicator(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_RightSlide_indicator'])).click()
