from src import utils as u
from src.pages.home import HomePage


class TestHomePage(u.WebDriverSetUp):

######################################## Homepage Testing #####################################################################

    def test_slideshow_right_arrow(self):
        HomePage.click_right_arrow_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]").get_attribute("class"), "active")

    def test_slideshow_left_arrow(self):
        HomePage.click_left_arrow_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]").get_attribute("class"), "active")

    def test_leftside_indicator(self):
        HomePage.click_leftslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[1]").get_attribute("class"), "active")

    def test_middleside_indicator(self):
        HomePage.click_midleslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[2]").get_attribute("class"), "active")

    def test_rightside_indicator(self):
        HomePage.click_rightslide_indicator(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/nav/div[2]/div/ol/li[3]").get_attribute("class"), "active")


    def test_match_product_links_image_title(self):
        """
        Homepage - Products - Matching products links in homepage
        :return:
        """
        products_images = HomePage.get_all_products_images_in_grid(self)
        products_titles = HomePage.get_all_products_titles_in_grid(self)

        images = list()
        titles = list()

        for prod in products_images:
            images.append(prod.get_attribute('href'))

        for prod in products_titles:
            titles.append(prod.get_attribute('href'))

        for i in range(len(images)):
            try:
                self.assertEqual(images[i], titles[i])
            except AssertionError:
                print(f"Products' title and image are not matching the same link.\n This is this product according to images: {images[i]} \nand this is the product according to titles: {titles[i]} \n")


    def test_match_product_links_image_title_next_page(self):
        """
        Homepage - Products - Matching products links in the next page
        :return:
        """
        u.sleep(5)
        HomePage.click_next_button(self)
        u.sleep(5)
        products_images = HomePage.get_all_products_images_in_grid(self)
        products_titles = HomePage.get_all_products_titles_in_grid(self)

        images = list()
        titles = list()

        for prod in products_images:
            images.append(prod.get_attribute('href'))

        for prod in products_titles:
            titles.append(prod.get_attribute('href'))

        if len(images) == len(titles):
            for i in range(len(images)):
                try:
                    self.assertEqual(images[i], titles[i])

                except AssertionError:
                    raise AssertionError(f"Products' title and image are not matching the same link.\n This is this product according to images: {images[i]} \nand this is the product according to titles: {titles[i]}")


