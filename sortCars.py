from HiltonCars import HiltonCars
from AvailableCars import AvailableCars

def getCars():
    hiltonCars = HiltonCars()
    availableCars = AvailableCars()

    hCars = hiltonCars.getCars()
    aCars = availableCars.getCars()

    cars = hCars
    cars.extend(aCars)

    return cars

def topFive(arr):
    if len(arr) > 5:
        arr = arr[:5]
    return arr

def topByCheapest(cars):
    top = sorted(cars, key=lambda car: car.price)
    return topFive(top)

def topByAge(cars):
    top = sorted(cars, key=lambda car: car.year, reverse=True)
    return topFive(top)

def getTopCars():
    cars = getCars()
    cheapest = topByCheapest(cars)
    newest = topByAge(cars)
    topCars = {
        "cheapest" : cheapest,
        "newest" : newest
    }
    best = set(topCars["cheapest"]).intersection(topCars["newest"])
    if best:
        topCars['topMatch'] = best
    return topCars
