import unittest
from src import utils as u
from pages.home import HomePage
from pages.contact import ContactModal

class TestContactModal(unittest.TestCase):

    def test_valid_message_send(self):
        ContactModal.set_contact_email(self, "Jhon237@gmail.com")
        ContactModal.set_contact_name(self, "Jhon")
        ContactModal.set_message(self, "Hello everyone! \nYou have too many bugs")
        ContactModal.click_send_message_btn(self)
        
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_invalid_email_message_send(self):
        ContactModal.set_contact_email(self, "b!fg")
        ContactModal.set_contact_name(self, "Jhon")
        ContactModal.set_message(self, "Hello everyone! \nYou have to many bugs")
        ContactModal.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_invalid_name_message_send(self):
        ContactModal.set_contact_email(self, "Jhon237@gmail.com")
        ContactModal.set_contact_name(self, 24324)
        ContactModal.set_message(self, "Hello everyone! \nYou have to many bugs")
        ContactModal.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_invalid_message_without_char(self):
        ContactModal.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_name_length_more_than_10_char(self):
        ContactModal.set_contact_email(self, "Jhon237@gmail.com")
        ContactModal.set_contact_name(self, "asd"*4)
        ContactModal.set_message(self, "Hello everyone! \nYou have to many bugs")
        ContactModal.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_message_length_more_than_256_char(self):
        ContactModal.set_contact_email(self, "Jhon237@gmail.com")
        ContactModal.set_contact_name(self, "Jhon")
        ContactModal.set_message(self, "Hello everyone!" * 130)
        ContactModal.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_X_btn(self):
        ContactModal.click_X_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade")

    def test_close_btn(self):
        ContactModal.click_close_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade")

    def test_send_message_btn(self):
        ContactModal.set_contact_email(self, "Jhon237@gmail.com")
        ContactModal.set_contact_name(self, "Jhon")
        ContactModal.set_message(self, "Hello everyone! \nYou have to many bugs")
        ContactModal.click_send_message_btn(self)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()
