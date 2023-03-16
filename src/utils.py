import selenium
import unittest


from selenium import webdriver as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service as Service
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.edge.options import Options as OptionsEdge

from time import sleep


class WebDriverSetUp(unittest.TestCase):

    def setUp(self) -> None:
        try:
            self.url = 'https://demoblaze.com/index.html'
            # chromedriver_path = 'drivers/chromedriver.exe'
            # options.add_argument("--headless")

            # driver_option = input(
            #     "Choose browser to test with: Chrome, Edge, Firefox \n NOTE: The browser must be installed on your machine... ").lower()

            options = OptionsChrome()
            options.add_argument("--disable-extensions")
            self.driver = WebDriver.Chrome(options=options)

            # if driver_option == 'chrome':
            #     options = OptionsChrome()
            #     options.add_argument("--disable-extensions")
            #     self.driver = WebDriver.Chrome(options=options)
            #
            # elif driver_option == 'firefox':
            #     options = OptionsFirefox()
            #     options.add_argument("--disable-extensions")
            #     self.driver = WebDriver.Firefox(executable_path=r'/src/drivers/geckodriver.exe', options=options)  # requires firefox installed in the machine
            #
            # elif driver_option == 'edge':
            #     options = OptionsEdge()
            #     options.add_argument("--disable-extensions")
            #     self.driver = WebDriver.Edge(options=options)
            #
            # elif driver_option == 'brave':
            #     options = OptionsChrome()
            #     options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
            #     self.driver = WebDriver.Chrome(chrome_options=options)

            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get(self.url)


        except AssertionError:
            self.driver.quit()

        except ResourceWarning:
            print("Invalid WebDriver, something there went wrong")
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()


def open_new_tab(driver, url):
    driver.switch_to.new_window('tab')
    sleep(1)
    driver.get(url)
    sleep(1)

def close_tab(driver):
    pass

if __name__ == '__main__':
    unittest.main()


