import random

from src import utils as u


class HomepageLocator:
    locHome = dict()

    # Home
    # Categories
    locHome['Home_Phones'] = (u.By.XPATH, '//a[text()="Phones"]')
    locHome['Home_Laptops'] = (u.By.XPATH, '//a[text()="Laptops"]')
    locHome['Home_Monitors'] = (u.By.XPATH, '//a[text()="Monitors"]')

    # Home
    # Items
    locHome['Items_Collection'] = (u.By.CSS_SELECTOR, '#tbodyid > div')  # item collection

    # Home
    # Navigation buttons
    locHome['NavBtn_Previous'] = (u.By.XPATH, "/html/body/div[5]/div/div[2]/form/ul/li[1]/button")
    locHome['NavBtn_Next'] = (u.By.XPATH, "/html/body/div[5]/div/div[2]/form/ul/li[2]/button")

    # Home
    # Slideshow buttons
    locHome['Slide_Right_Arrow'] = (u.By.XPATH, "/html/body/nav/div[2]/div/a[2]/span[1]")
    locHome['Slide_Left_Arrow'] = (u.By.XPATH, "/html/body/nav/div[2]/div/a[1]/span[1]")
    locHome['Slide_LeftSlide_indicator'] = (u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]")
    locHome['Slide_MiddleSlide_indicator'] = (u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]")
    locHome['Slide_RightSlide_indicator'] = (u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]")

    locHome['Random_Product'] = (u.By.XPATH, f'//*[@id="tbodyid"]/div[{random.randint(1,9)}]/div/div/h4/a')
    locHome['All_Products_Grid'] = (u.By.XPATH, '//*[@id="tbodyid"]')       # the grid itself
    locHome['Products_In_Grid'] = (u.By.XPATH, '//*[@id="tbodyid"]/div')    # list of products in the grid
    locHome['Products_Images_In_Grid'] = (u.By.XPATH, '//*[@id="tbodyid"]/div/div/a')    # list of products images in the grid
    locHome['Products_Title_In_Grid'] = (u.By.XPATH, '//*[@id="tbodyid"]/div/div/div/h4/a')    # list of products titles in the grid
