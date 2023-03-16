import src.utils as u
from src.locators.locators_index import HomepageLocator
from src.locators.locators_index import ProductLocator
from src.locators.locators_index import CartLocator
from src.pages.header import HeaderPage

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Random_Product'])).click()
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ProductLocator.locProd['Product_Add_To_Cart'])).click()

    def remove_product_from_cart(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Delete_Item'])).click()


    def click_place_order(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Place_Order_Button'])).click()


    def click_purchase(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Purchase_Button'])).click()


    def click_ok_after_purchase(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['OK_Purchase_Button'])).click()


    def from_homepage_to_item_in_cart(self):
        CartPage.add_product_to_cart(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        HeaderPage.click_cart_btn(self)


    def order_modal_fields(self):
        self.order_modal = dict()
        self.order_modal['name'] = self.driver.find_element(u.By.XPATH, '//*[@id="name"]')
        self.order_modal['country'] = self.driver.find_element(u.By.XPATH, '//*[@id="country"]')
        self.order_modal['city'] = self.driver.find_element(u.By.XPATH, '//*[@id="city"]')
        self.order_modal['card'] = self.driver.find_element(u.By.XPATH, '//*[@id="card"]')
        self.order_modal['month'] = self.driver.find_element(u.By.XPATH, '//*[@id="month"]')
        self.order_modal['year'] = self.driver.find_element(u.By.XPATH, '//*[@id="year"]')

        return self.order_modal