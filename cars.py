from utils import *

cars = []


def addCar():
    try:
        brand = getText("Brand: ")
        model = getText("Model: ")
        price = getFloat("Price: ")
        year = getInt("Year: ")
        color = getText("Color: ")

        if year < 1886 or year > 2026:
            raise ValueError("year is not correct")

        if price <= 0:
            raise ValueError("price is not correct")

        car = {
            "id": max([c["id"] for c in cars], default=0) + 1,
            "brand": brand,
            "model": model,
            "price": price,
            "year": year,
            "color": color
        }

        cars.append(car)
        print("car added successfully.")

    except ValueError as e:
        print("some error occurred:", e)