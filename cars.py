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

def showAllCars():
    try:
        if not cars:
            print("there is no car.")
            return

        for car in cars:
            showCar(car)

    except Exception as e:
        print("Error:", e)

def updateCar():
    try:
        if not cars:
            print("there is no car.")
            return

        carID = getInt("enter car ID: ")

        car = None

        for i in cars:
            if i["id"] == carID:
                car = i
                break

        if car is None:
            raise ValueError("car not found")

        showCar(car)

        print("""
        1. Price
        2. Color
        """)

        choice = getInt("enter choice: ")

        if choice == 1:
            newPrice = getFloat("enter new price: ")

            if newPrice <= 0:
                raise ValueError("price is not correct")

            car["price"] = newPrice

        elif choice == 2:
            car["color"] = getText("enter new color: ")

        else:
            raise ValueError("wrong choice")

        print("car updated.")

    except ValueError as e:
        print("Error:", e)

def deleteCar():
    try:
        if not cars:
            print("there is no car.")
            return

        deletedID = getInt("enter car ID: ")

        for car in cars:
            if car["id"] == deletedID:
                cars.remove(car)
                print("car deleted.")
                return

        raise ValueError("car not found")

    except ValueError as e:
        print("Error:", e)

def filterByPrice():
    try:
        if not cars:
            raise ValueError("there is no car.")

        choice = getInt(
            "1. Expensive to cheap\n"
            "2. Cheap to expensive\n"
            "Choose: "
        )

        if choice == 1:
            sortedCars = sorted(
                cars, key=lambda c: c["price"], reverse=True
            )

        elif choice == 2:
            sortedCars = sorted(
                cars, key=lambda c: c["price"]
            )

        else:
            raise ValueError("wrong choice")

        for car in sortedCars:
            showCar(car)

    except ValueError as e:
        print("Error:", e)

def filterByYear():
    try:
        if not cars:
            raise ValueError("there is no car.")

        choice = getInt(
            "1. Newest to oldest\n"
            "2. Oldest to newest\n"
            "Choose: "
        )

        if choice == 1:
            sortedCars = sorted(
                cars, key=lambda c: c["year"], reverse=True
            )

        elif choice == 2:
            sortedCars = sorted(
                cars, key=lambda c: c["year"]
            )

        else:
            raise ValueError("wrong choice")

        for car in sortedCars:
            showCar(car)

    except ValueError as e:
        print("Error:", e)