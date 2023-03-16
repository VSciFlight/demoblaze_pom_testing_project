from src import utils as u


class ProductLocator:

    locProd = dict()

    # Product
    locProd['Product_Add_To_Cart'] = (u.By.XPATH, '//a[text()="Add to cart"]')
    locProd['Product_Undefined_Headline'] = (u.By.XPATH, '//h2[text()="undefined"]')
