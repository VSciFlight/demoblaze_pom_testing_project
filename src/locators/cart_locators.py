import src.utils as u

class CartLocator:

        locCart = dict()

        locCart['Cart_Rows'] = (u.By.XPATH, '//*[@id="tbodyid"]/tr')
        locCart['Place_Order_Button'] = (u.By.XPATH, '//*[text()="Place Order"]')
        locCart['Delete_Item'] = (u.By.XPATH, '//*[@id="tbodyid"]/tr/td[4]/a')
        locCart['Order_Modal'] = (u.By.XPATH, '//*[@id="orderModal"]')
        locCart['Purchase_Button'] = (u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
        locCart['OK_Purchase_Button'] = (u.By.XPATH, '/html/body/div[10]/div[7]/div/button')

