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

def showCar(car):
    try:
        print("-" * 20)
        print(f"ID: {car['id']}")
        print(f"Brand: {car['brand']}")
        print(f"Model: {car['model']}")
        print(f"Price: {car['price']}")
        print(f"Year: {car['year']}")
        print(f"Color: {car['color']}")
        print("-" * 20)

    except (KeyError, TypeError) as e:
        print("car data error:", e)