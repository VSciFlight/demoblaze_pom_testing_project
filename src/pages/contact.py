from src import utils as u
from src.locators.locators_index import ContactLocator

class ContactModal:

    def __init__(self, driver):
        self.driver = driver

    def set_contact_email(self, email):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ContactLocator.locContact['Contact_Email_fld'])).send_keys(email)

    def set_contact_name(self, name):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ContactLocator.locContact['Contact_Name_fld'])).send_keys(name)

    def set_message(self, message):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ContactLocator.locContact['Message_fld'])).send_keys(message)

    def click_X_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ContactLocator.locContact['X_btn'])).click()

    def click_close_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ContactLocator.locContact['Close_btn'])).click()

    def click_send_message_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ContactLocator.locContact['Send_Message_btn'])).click()
