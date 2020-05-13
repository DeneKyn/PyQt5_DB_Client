class Product:
    def __init__(self, info):
        self.info = info
        self.id_offer = info.get('id', None)
        self.id = info.get('id_product', None)
        self.category = info.get('category', None)
        self.id_category = info.get('id_category', None)
        self.manufacturer = info.get('manufacturer', None)
        self.model = info.get('name', None)
        self.price = info.get('price', None)
        self.offers = info.get('offers', None)
        self.date_to_storage = info.get('date_to_storage', None)

