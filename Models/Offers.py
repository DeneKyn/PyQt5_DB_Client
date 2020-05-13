class Offers:
    def __init__(self, info):
        self.info = info
        self.id = info.get('id', None)
        self.price = info.get('price', None)
        self.company_name = info.get('company_name', None)
        self.sales_amount = info.get('sales_amount', None)
        self.storage_amount = info.get('storage_amount', None)
        self.amount = info.get('amount', None)


