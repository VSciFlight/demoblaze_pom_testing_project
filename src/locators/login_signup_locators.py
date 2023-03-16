from src import utils as u


class LoginLocator:

    # Login and Signup
    locLog = dict()

    locLog['Login_Username'] = (u.By.XPATH, '//*[@id="loginusername"]')
    locLog['Login_Password'] = (u.By.XPATH, '//*[@id="loginpassword"]')
    locLog['Login_Button'] = (u.By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

    locLog['Signup_Username'] = (u.By.XPATH, '//*[@id="sign-username"]')
    locLog['Signup_Password'] = (u.By.XPATH, '//*[@id="sign-password"]')
    locLog['Signup_Button'] = (u.By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    locLog['Welcome'] = (u.By.XPATH, '//*[@id="nameofuser"]')
