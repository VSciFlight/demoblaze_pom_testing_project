from src import utils as u
from src.pages.header import HeaderPage
from src.locators.locators_index import CartLocator
from src.locators.locators_index import HomepageLocator
from src.locators.locators_index import ProductLocator
from src.pages.cart import CartPage
from src.pages.product import ProductPage

class TestCartPage(u.WebDriverSetUp):

    def test_cart_recovery(self):
        CartPage.add_product_to_cart(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Product added")
        alert.accept()


        HeaderPage.click_cart_btn(self)
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Cart_Rows']))

        self.assertEqual(self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/tr').get_attribute("class"), "success")

        self.driver.quit()
        u.WebDriverSetUp.setUp(self)

        HeaderPage.click_cart_btn(self)

        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Cart_Rows']))

        except:
            self.assertTrue(self.driver.find_elements(u.By.XPATH, '//*[@id="tbodyid"]/tr'), msg="No items in the cart")



#######################################################################################################

    def test_add_item_to_cart(self):
        CartPage.add_product_to_cart(self)
        u.WDW(self.driver, 3).until(u.EC.alert_is_present())
        self.alert = self.driver.switch_to.alert
        self.alert.accept()

        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(3)

        self.assertTrue(u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Cart_Rows'])))

    def test_remove_item_from_cart(self):
        CartPage.add_product_to_cart(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(2)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/tr/td[4]/a').click()  #delete button
        u.sleep(2)

        cart_row = self.driver.find_elements(u.By.XPATH, '//*[@id="tbodyid"]/tr')

        self.assertFalse(cart_row)



    def test_place_order_button(self):

        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Random_Product'])).click()
        u.sleep(3)

        ProductPage.add_product_to_cart(self)
        u.WDW(self.driver, 3).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        HeaderPage.click_cart_btn(self)
        CartPage.click_place_order(self)
        u.sleep(3)

        modal = self.driver.find_element(u.By.XPATH, '//*[@id="orderModal"]')
        self.assertEqual(modal.get_attribute('class'), 'modal fade show')



    def test_purchase_with_valid_data(self):
        """
        test purchase details with valid data
        :return:
        """
        CartPage.from_homepage_to_item_in_cart(self)
        CartPage.click_place_order(self)

        u.sleep(2)
        self.order_modal = CartPage.order_modal_fields(self)

        self.order_modal['name'].send_keys("Nir Peled")
        self.order_modal['country'].send_keys("Israel")
        self.order_modal['city'].send_keys("Shoam")
        self.order_modal['card'].send_keys("51159876543654")
        self.order_modal['month'].send_keys("14.6")
        self.order_modal['year'].send_keys("2001")

        u.sleep(1)
        CartPage.click_purchase(self)
        u.sleep(1)

        confirm_message = self.driver.find_element(u.By.XPATH, '/html/body/div[10]/h2').text
        self.assertEqual(confirm_message, "Thank you for your purchase!")

    def test_ok_button_valid(self):
        """
        testing the ok button after purchase leads me to the homepage
        :return:
        """
        CartPage.from_homepage_to_item_in_cart(self)
        CartPage.click_place_order(self)

        u.sleep(2)
        self.order_modal = CartPage.order_modal_fields(self)

        self.order_modal['name'].send_keys("Ashtray Maze")
        self.order_modal['country'].send_keys("New York")
        self.order_modal['city'].send_keys("Control Bureau")
        self.order_modal['card'].send_keys("51159876543654")
        self.order_modal['month'].send_keys("14.6")
        self.order_modal['year'].send_keys("2001")

        u.sleep(1)
        CartPage.click_purchase(self)
        u.sleep(1)

        CartPage.click_ok_after_purchase(self)
        u.sleep(2)
        self.assertEqual(self.driver.current_url, u.url)

    def test_purchase_invalid_data(self):
        """
        test purchase with invalid data, random data
        :return:
        """
        CartPage.from_homepage_to_item_in_cart(self)
        CartPage.click_place_order(self)

        u.sleep(2)
        self.order_modal = CartPage.order_modal_fields(self)

        self.order_modal['name'].send_keys(u.rand_string())
        self.order_modal['country'].send_keys(u.rand_string())
        self.order_modal['city'].send_keys(u.rand_string())
        self.order_modal['card'].send_keys(u.rand_string())
        self.order_modal['month'].send_keys(u.rand_string())
        self.order_modal['year'].send_keys(u.rand_string())

        u.sleep(1)
        CartPage.click_purchase(self)
        u.sleep(1)

        confirm_message = self.driver.find_element(u.By.XPATH, '/html/body/div[10]/h2').text
        self.assertNotEqual(confirm_message, "Thank you for your purchase!")


    def test_empty_purchase_details(self):
        """
        I expect the form not to transfer me ahead
        :param self:
        :return:
        """

        CartPage.from_homepage_to_item_in_cart(self)
        CartPage.click_place_order(self)
        u.sleep(2)
        self.order_modal = CartPage.order_modal_fields(self)

        u.sleep(1)
        CartPage.click_purchase(self)
        u.sleep(1)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        self.assertEqual(alert.text, 'Please fill out Name and Creditcard.')

    def test_min_purchase_details(self):
        """
        The site asked me to fill only name and creditcard.
        this test will valid it
        :param self:
        :return:
        """

        CartPage.from_homepage_to_item_in_cart(self)
        CartPage.click_place_order(self)

        u.sleep(2)
        self.order_modal = CartPage.order_modal_fields(self)

        self.order_modal['name'].send_keys("Nir Peled")
        self.order_modal['card'].send_keys("51159876543654")

        u.sleep(1)
        CartPage.click_purchase(self)
        u.sleep(1)

        confirm_message = self.driver.find_element(u.By.XPATH, '/html/body/div[10]/h2').text
        self.assertEqual(confirm_message, "Thank you for your purchase!")



    def test_open_cart_url_directly(self):
        """
        A fun bug I found.
        I found out if you open the cart url directly (without going through in homepage)
        the cart rows just populate for some point
        :return:
        """
        self.driver.quit()

        self.driver = u.WebDriver.Chrome()
        self.driver.get('https://demoblaze.com/cart.html')
        u.sleep(10)

        cart_rows = self.driver.find_elements(u.By.XPATH, '//*[@id="tbodyid"]/tr')
        self.assertFalse(len(cart_rows), msg=f'{len(cart_rows)} orders')     # I should get no items





