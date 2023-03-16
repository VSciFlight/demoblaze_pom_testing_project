from src import utils as u
from src.locators.locators_index import AboutUsLocator
from src.pages.header import HeaderPage

class TestAboutUsPage(u.WebDriverSetUp):

    ###################################### About us tests ###################################################

    def test_play_button(self):
        HeaderPage.click_about_us_btn(self)
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(AboutUsLocator.abtloc['Play_Button'])).click()
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(AboutUsLocator.abtloc['Pause_Button']))

        pause_play = self.driver.find_element(u.By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/div[4]/button[1]")

        self.assertTrue(pause_play)

