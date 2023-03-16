from src import utils as u


class HeadLocator:

    locHeader = dict()
    # Header
    locHeader['Head_Home'] = (u.By.XPATH, '//a[text()="Home "]')
    locHeader['Head_Contact'] = (u.By.XPATH, '//a[text()="Contact"]')
    locHeader['Head_About_Us'] = (u.By.XPATH, '//a[text()="About us"]')
    locHeader['Head_Cart'] = (u.By.XPATH, '//a[text()="Cart"]')
    locHeader['Head_Login'] = (u.By.XPATH, '//a[text()="Log in"]')
    locHeader['Head_Logout'] = (u.By.XPATH, '//a[text()="Log out"]')
    locHeader['Head_Signup'] = (u.By.XPATH, '//a[text()="Sign up"]')
    locHeader['Head_Logo'] = (u.By.XPATH, "/html/body/nav/a")

