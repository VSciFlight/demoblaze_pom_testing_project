import string

from src.pages.login_sign_up import LoginSignUpPage
from src.locators.locators_index import LoginLocator
from src import utils as u



class TestLoginSignUp(u.WebDriverSetUp):

    username = u.rand_string(n=10)
    password = u.rand_string(group=string.printable, n=10)

    valid_username = "qazwsxedcqaz"
    valid_password = "qazwsxedcqaz"


    # @u.allure.description("Tests Sign Up")
    # @u.allure.severity(severity_level="HIGH")
    def test_sign_up(self):
        """
        Sign up - Modal - Create a user using the form
        :return:
        """
        LoginSignUpPage.sign_up(self, self.username, self.password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Sign up successful.")
            alert.accept()

        except:
            print("The user exists")
            assert alert.text == "This user already exist."
            alert.accept()


    def test_sign_up_existing_user(self):
        """
        Sign up - Modal - Create an existing user (N)
        :return:
        """
        LoginSignUpPage.sign_up(self, self.valid_username, self.valid_password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "This user already exist.")
        alert.accept()



    def test_sign_up_no_values(self):
        LoginSignUpPage.sign_up(self, "", "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_sign_up_lot_chars(self):
        """
        Sign up - Modal - Create a user having more than 10 chars
        Test about username length, the requirement said it should contain less than 10 chars
        however it seems to accept more than 10 chars
        :return:
        """
        tmp_user = u.rand_string(n=11)
        LoginSignUpPage.sign_up(self, tmp_user, self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertNotEqual(alert.text, "Sign up successful.", msg="Able to create a user above 10 chars in username")

        alert.accept()



    def test_sign_up_user_only(self):
        """
        Sign up - Modal - Create account using one field (N)
        test sign up with username only,
        The error I should get is indicator of "Password missing" or something along these lines
        However I don't get those and it returns "Please fill out Username and Password." as alert message.
        :return:
        """
        LoginSignUpPage.sign_up(self, self.username, "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert


        self.assertEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()


    def test_sign_up_pass_only(self):
        """
        Sign up - Modal - Create account using one field (N)
        test sign up with password only,
        The error I should get is indicator of "Password missing" or something along these lines
        However I don't get those and it returns "Please fill out Username and Password." as alert message.
        :return:
        """
        LoginSignUpPage.sign_up(self, "", self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertNotEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()



    def test_login_after_sign_up(self):
        """
        Log in - Modal - Log into new account
        Log in - Modal - Log into existing account
        Log in - Modal - Login using special characters (N, htmlchars)
        Tests you can create a user and log into it
        :return:
        """
        LoginSignUpPage.sign_up(self, self.username, self.password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "Sign up successful.")
        alert.accept()

        LoginSignUpPage.login_acc(self, self.username, self.password)

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.username)

    def test_login_valid(self):
        """
        Log in - Modal - Log into existing account

        :return:
        """
        LoginSignUpPage.login_acc(self, self.valid_username, self.valid_password)

        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)
        # I would expect the site to tell me I miss only the username


    def test_login_no_values(self):
        """
        Log in - Modal - Log into non-existing account (N)
        Test login with no values
        :return:
        """
        LoginSignUpPage.login_acc(self, "", "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()



    def test_login_invalid_user(self):
        """
        I would expect the site to tell me the user doesn't exist before telling me there is no password
        :return:
        """
        LoginSignUpPage.login_acc(self, self.username, "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "User does not exist.")
        alert.accept()



    def test_login_invalid_password(self):
        LoginSignUpPage.login_acc(self, self.valid_username, self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, "Wrong password.")
        alert.accept()
        # I would expect the site to tell me the user doesn't exist


    def test_login_pass_only(self):
        """
        Log in - Modal - Login using one field (N)

        :return:
        """
        LoginSignUpPage.login_acc(self, "", self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertNotEqual(alert.text, "Please fill out Username and Password.")
        alert.accept()
        # I would expect the site to tell me I miss only password


    def test_autolog_in_new_tab(self):
        """
        Log In - Cookie - Log into account, close the tab and enter the site again in a new tab
        Log In - Cookie - Log into account, open a new tab with the site and user will be logged

        The case is logging into the site and then opening new tab and checking
        wether is connected user is connected or not
        :return:
        """

        LoginSignUpPage.login_acc(self, self.valid_username, self.valid_password)

        u.open_new_tab(self.driver, self.url)

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)


    def test_autolog_after_quitting_browser(self):
        """
        Log In - Cookie - User will be logged in after he logged in, closed the browser and open the site again in a browser
        The case is logging into account and then closing the browser
        The expectation is to be logged in when logging into the site again

        FAILED
        :return:
        """
        LoginSignUpPage.login_acc(self, self.valid_username, self.valid_password)
        u.sleep(2)

        self.driver.quit()
        u.sleep(1)
        u.WebDriverSetUp.setUp(self)

        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Welcome']))
            welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')
            self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)
        except u.selexcep.TimeoutException:
            raise AssertionError("No sign of user being logged in")

    def test_user_cookie_change(self):
        """
        Log In - Cookie - logging into account using cookies (N)

        Test that takes the cookie and test if the user can use the cookie to log in using cookies
        SECURITY MEASURE

        :return:
        """
        LoginSignUpPage.login_acc(self, self.valid_username, self.valid_password)
        u.sleep(1)

        user_data = self.driver.get_cookies()

        self.driver.quit()
        u.sleep(2)

        options = u.WebDriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        self.driver = u.WebDriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(self.url)

        for cookie in user_data:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(LoginLocator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.valid_username)