import src.utils as u
from src.locators.locators_index import HomepageLocator
from src.locators.locators_index import ProductLocator
from src.locators.locators_index import CartLocator

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(HomepageLocator.locHome['Random_Product'])).click()
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(ProductLocator.locProd['Product_Add_To_Cart'])).click()

    def remove_product_from_cart(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(CartLocator.locCart['Delete_Item']))

