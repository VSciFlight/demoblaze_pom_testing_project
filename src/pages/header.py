from src import utils as u
from src.locators.locators_index import HeadLocator


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

################################################## Header ############################################################################################################

    def click_home_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Home'])).click()

    def click_contact_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Contact'])).click()

    def click_about_us_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_About_Us'])).click()

    def click_cart_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Cart'])).click()

    def click_logout_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Logout'])).click()

    def click_signup_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Signup'])).click()

    def click_logo_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Logo'])).click()