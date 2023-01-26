class Flight:

    def __init__(self, number: str):

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError("the first 2 char must be uppercase")

        if not (number[2:].isdigit() and int(number[2:]) < 1000):
            raise ValueError("Invalid number please try later")

        self._number = number

    def get_flight_number(self):
        return self._number
