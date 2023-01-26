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

    def airline(self):
        return self._number[:2]


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def get_registration(self):
        print(self)
        return self._registration

    def get_model(self):
        return self._model
