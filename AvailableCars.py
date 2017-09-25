from lxml import html
from Car import Car 
import requests
import re

class AvailableCars(object):

    def __init__(self):
        self.cars = []
        self.url = "http://www.availablecar.com"

    def getTree(self):
        page = requests.get(self.url + "/Search/1?s=&p=%7C4999")
        tree = html.fromstring(page.content)
        return tree

    def getElements(self):
        tree = self.getTree()
        cars = []
        price = tree.xpath('//div[@class="main-section"]/div[@id="searchResultsContainer"]/div[@id="searchResultsLeftPanel"]/ul/li/div[contains(concat(" ",@class," ")," carDetails ")]/div[contains(concat(" ",@class, " "),"searchResultsItemFinance")]/span[@class="carheader"]/span/text()')
        year = tree.xpath('//div[@class="main-section"]/div[@id="searchResultsContainer"]/div[@id="searchResultsLeftPanel"]/ul/li/div[contains(concat(" ",@class," ")," carDetails ")]/span[contains(concat(" ",@class," "),"searchResultsItemDetails")]/text()')
        name = tree.xpath('//div[@class="main-section"]/div[@id="searchResultsContainer"]/div[@id="searchResultsLeftPanel"]/ul/li/div[contains(concat(" ",@class," ")," carDetails ")]/a/text()')
        url = tree.xpath('//div[@class="main-section"]/div[@id="searchResultsContainer"]/div[@id="searchResultsLeftPanel"]/ul/li/div[contains(concat(" ",@class," ")," carDetails ")]/a/@href')
        for i in range(len(price)):
            reserved = tree.xpath('//div[@class="main-section"]/div[@id="searchResultsContainer"]/div[@id="searchResultsLeftPanel"]/ul/li['+str(i+1)+']/div[contains(concat(" ",@class," "),"searchResultsImageContainer")]/a[@class="searchResultsCarImage"]/span')
            if not len(reserved) > 0:
               price[i] = price[i].replace('£','')
               y = re.findall(r"[^-\s]\d{3}", year[i], flags=0)
               year[i] = int(y[0])
               car = Car("Available", int(price[i]), year[i], name[i], self.url + url[i]);
               cars.append(car);
        self.cars = cars

    def getCars(self):
        self.getElements()
        return self.cars

#/html/body/div[@class="main-section"]/div[@id="searchResultsContainer"]/div[@id="searchResultsLeftPanel"]/ul/li[1]/div[1]/a/span
