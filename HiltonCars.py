# encoding=utf8  
from lxml import html
from Car import Car 
import requests

class HiltonCars(object):

    def __init__(self):
        self.cars = []
        self.url = "http://www.hiltongarage.co.uk"

    def getTree(self):
        trees = []
        page = requests.get(self.url + "/used-cars/?COGPriceFrom=2000&COGPriceTo=5000")
        tree = html.fromstring(page.content)
        trees.append(tree)
        listOfPages = tree.xpath('//form/div[@id="controls-wrapper"][1]/div[@id="controls-pagination"]/div[@id="pagination"]/ul[@class="COGPager"]/li[@class="COGPagerItem"]/a/@href')
        if listOfPages:
            for nextPage in listOfPages:
                page = requests.get(self.url + nextPage)
                tree = html.fromstring(page.content)
                trees.append(tree)
        return trees
    
    def getElements(self):
        trees = self.getTree()
        cars = []
        for tree in trees:
            price = tree.xpath('//section[@class="used-list-vehicle"]//div[@class="used-list-price"]//p[1]//span[@class="large"]/text()')
            year = tree.xpath('//section[@class="used-list-vehicle"]//table[@class="used-list-spec"]//tr[3]//td[1]/text()')
            name = tree.xpath('//section[@class="used-list-vehicle"]//div[@class="used-list-right"]//h2[@class="used-left-title"]/text()')
            url = tree.xpath('//section[@class="used-list-vehicle"]//div[@class="used-list-left"]//a[1]/@href')
            for i in range(len(price)):
                price[i] = price[i].replace(',', '')
                price[i] = price[i].replace('£', '')
                car = Car("Hilton", int(price[i]), int(year[i]), name[i], self.url + url[i]);
                cars.append(car);
        self.cars = cars
    
    def getCars(self):
        self.getElements()
        return self.cars
