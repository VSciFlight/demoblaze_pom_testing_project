import unittest

from src import utils as u
from src.pages.header import HeaderPage
from src.pages.home import HomePage


class TestHomePage(u.WebDriverSetUp):

###################################### Header Buttons Tests ###################################################
    def test_home_btn(self):
        HeaderPage.click_home_btn(self)
        self.assertEqual(self.driver.current_url, "https://www.demoblaze.com/index.html")

    def test_contact_btn(self):

        HeaderPage.click_contact_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[1]").get_attribute("id"), 'exampleModal')

    def test_about_us_btn(self):
        HeaderPage.click_about_us_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[4]").get_attribute("id"), "videoModal")

    def test_cart_btn(self):
        HeaderPage.click_cart_btn(self)
        self.assertEqual(self.driver.current_url, "https://www.demoblaze.com/cart.html")

    def test_login_btn(self):
        HeaderPage.click_login_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[3]").get_attribute("id"), "logInModal")

    def test_signup_btn(self):
        HeaderPage.click_signup_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[2]").get_attribute("id"), "signInModal")

    def test_logo_btn(self):
        HeaderPage.click_logo_btn(self)
        self.assertEqual(self.driver.current_url, "https://www.demoblaze.com/index.html")

######################################################################################################################################

######################################## Homepage Testing #####################################################################

    def test_slideshow_right_arrow(self):

        HomePage.click_right_arrow_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]").get_attribute("class"), "active")

    def test_slideshow_left_arrow(self):
        HomePage.click_left_arrow_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]").get_attribute("class"), "active")

    def test_leftside_indicator(self):
        HomePage.click_leftslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]").get_attribute("class"), "active")

    def test_midleside_indicator(self):
        HomePage.click_midleslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]").get_attribute("class"), "active")

    def test_rightside_indicator(self):
        HomePage.click_rightslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]").get_attribute("class"), "active")