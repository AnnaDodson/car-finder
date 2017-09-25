class Car(object):
    price = ''
    year = ''
    url = ''
    name = ''

    def __init__(self, shop, price, year, name, url):
        self.shop = shop
        self.price = price
        self.year = year
        self.name = name
        self.url = url

