from Models.Product import Product
from Models.Offers import Offers


class Purchase:
    def __init__(self, info):
        self.product = Product(info)
        self.offer = Offers(info)
        self.date_of_sale = info.get('date_of_sale', None)
        self.login = info.get('login', None)

