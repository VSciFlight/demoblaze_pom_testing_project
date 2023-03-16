import src.utils as u

class CartLocator:

        locCart = dict()

        locCart['Cart_Rows'] = (u.By.XPATH, '//*[@id="tbodyid"]/tr')

        locCart['Place_Order_Button'] = (u.By.XPATH, '//*[text()="Place Order"]')

        locCart['Delete_Item'] = (u.By.XPATH, '//*[@id="tbodyid"]/tr/td[4]/a')
