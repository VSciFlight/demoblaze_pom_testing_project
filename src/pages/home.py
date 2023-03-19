from src import utils as u
from src.locators.locators_index import HomepageLocator


class HomePage:

    def __init__(self, driver):
        self.driver = driver

#######################################################################################################################################################################

################################################################ Slideshow #################################################################################################

    def click_right_arrow_btn(self):
        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_Right_Arrow'])).click()
        except u.selexcep.TimeoutException:
            raise u.xceptions.HeadlessException

    def click_left_arrow_btn(self):
        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_Left_Arrow'])).click()
        except u.selexcep.TimeoutException:
            raise u.xceptions.HeadlessException

    def click_leftslide_indicator(self):
        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_LeftSlide_indicator'])).click()
        except u.selexcep.TimeoutException:
            raise u.xceptions.HeadlessException

    def click_middleslide_indicator(self):
        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_MiddleSlide_indicator'])).click()
        except u.selexcep.TimeoutException:
            raise u.xceptions.HeadlessException

    def click_rightslide_indicator(self):
        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Slide_RightSlide_indicator'])).click()
        except u.selexcep.TimeoutException:
            raise u.xceptions.HeadlessException

    def click_on_product(self):
        u.WDW(self.driver, 5).until(
            u.EC.visibility_of_element_located(HomepageLocator.locHome['NavBtn_Next'])).click()

    def click_next_button(self):
        u.WDW(self.driver, 5).until(
            u.EC.visibility_of_element_located(HomepageLocator.locHome['NavBtn_Next'])).click()

    def click_previous_button(self):
        u.WDW(self.driver, 5).until(
            u.EC.visibility_of_element_located(HomepageLocator.locHome['NavBtn_Previous'])).click()

    def get_all_products_images_in_grid(self):
        return u.WDW(self.driver, 5).until(u.EC.visibility_of_all_elements_located(HomepageLocator.locHome['Products_Images_In_Grid']))

    def get_all_products_titles_in_grid(self):
        return u.WDW(self.driver, 5).until(u.EC.visibility_of_all_elements_located(HomepageLocator.locHome['Products_Title_In_Grid']))