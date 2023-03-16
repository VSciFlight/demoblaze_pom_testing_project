import string
import random

from src.locators.locators_index import LoginLocator
from src.locators.locators_index import HeadLocator
from src import utils as u


class LoginSignUpPage:

    def __init__(self, driver):
        self.driver = driver

    def signup_set_usernsme(self, username):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Signup_Username'])).send_keys(username)

    def signup_set_password(self, password):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Signup_Password'])).send_keys(password)

    def click_signup(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Signup_Button'])).click()


    def login_set_usernsme(self, username):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Login_Username'])).send_keys(username)

    def login_set_password(self, password):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Login_Password'])).send_keys(password)

    def click_login(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Login_Button'])).click()



    def sign_up(self, username_name="", password_pass=""):
        """
        performs signup with details given
        :param driver:
        :param username_name:
        :param password_pass:
        :return:
        """

        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Signup'])).click()

        LoginSignUpPage.signup_set_usernsme(self, username_name)
        LoginSignUpPage.signup_set_password(self, password_pass)
        LoginSignUpPage.click_signup(self)



    def login_acc(self, username="", password=""):
        """
        performs login into existing account
        :param self:
        :param username:
        :param password:
        :return:
        """

        u.WDW(self.driver, 20).until(u.EC.visibility_of_element_located(HeadLocator.locHeader['Head_Login'])).click()

        LoginSignUpPage.login_set_usernsme(self, username)
        LoginSignUpPage.login_set_password(self, password)
        LoginSignUpPage.click_login(self)


    def rand_string(group=string.ascii_letters, n=10):
        """
        this function is taking a group of letters and then takes a number.
        it returns a string with random chars from the group in the length of the number  we provided
        :param group:
        :param n:
        :return:
        """
        return ''.join(random.choice(group) for i in range(n))
