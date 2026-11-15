from cars import addCar , showAllCars , updateCar , deleteCar , filterCars
from utils import *


def main():
    while True:
        try:
            print("""
--- CAR MANAGEMENT SYSTEM ---
1. Add Car
2. Show All Cars
3. Update Car
4. Delete Car
5. Filter / Sort Cars
6. Exit
            """)

            choice = getInt("enter your choice: ")

            if choice == 1:
                addCar()

            elif choice == 2:
                showAllCars()

            elif choice == 3:
                updateCar()

            elif choice == 4:
                deleteCar()

            elif choice == 5:
                filterCars()

            elif choice == 6:
                print("exiting program. Goodbye!")
                break

            else:
                print("invalid choice, try again.")

        except Exception as e:
            print("an error occurred:", e)


main()