def getInt(message):
    while True:
        try:
            value = input(message).strip()

            if value:
                return int(value)
            else:
                raise ValueError

        except ValueError:
            print("error, please enter int value.")