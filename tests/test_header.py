from src import utils as u
from src.pages.header import HeaderPage

class TestHeaderPage(u.WebDriverSetUp):

###################################### Header Buttons Tests ###################################################
    def test_home_btn(self):
        HeaderPage.click_home_btn(self)
        self.assertEqual(self.driver.current_url, "https://demoblaze.com/index.html")

    def test_contact_btn(self):
        HeaderPage.click_contact_btn(self)
        contact_modal = self.driver.find_element(u.By.XPATH, '//*[@id="exampleModal"]')
        self.assertEqual(contact_modal.get_attribute('class'), "modal fade show")

    def test_about_us_btn(self):
        HeaderPage.click_about_us_btn(self)
        about_modal = self.driver.find_element(u.By.XPATH, '//*[@id="videoModal"]')
        self.assertEqual(about_modal.get_attribute('class'), "modal fade show")

    def test_cart_btn(self):
        HeaderPage.click_cart_btn(self)
        self.assertEqual(self.driver.current_url, "https://demoblaze.com/cart.html")

    def test_login_btn(self):
        HeaderPage.click_login_btn(self)
        login_modal = self.driver.find_element(u.By.XPATH, '//*[@id="logInModal"]')
        self.assertEqual(login_modal.get_attribute('class'), "modal fade show")

    def test_signup_btn(self):
        HeaderPage.click_signup_btn(self)
        sign_up_modal = self.driver.find_element(u.By.XPATH, '//*[@id="signInModal"]')
        self.assertEqual(sign_up_modal.get_attribute('class'), "modal fade show")

    def test_logo_btn(self):
        HeaderPage.click_logo_btn(self)
        self.assertEqual(self.driver.current_url, "https://demoblaze.com/index.html")
