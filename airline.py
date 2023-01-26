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

    def get_settings_plan(self):
        return (range(1, self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


class Flight:

    def __init__(self, number: str, aircraft: Aircraft):

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError("the first 2 char must be uppercase")

        if not (number[2:].isdigit() and int(number[2:]) < 1000):
            raise ValueError("Invalid number please try later")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.get_settings_plan()
        self._seating = [{letter: None for letter in seats} for row in rows]

    def get_flight_number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def get_aircraft_model(self):
        return self._aircraft.get_model()

    def allocate_passenger(self, seat: str, passenger_name: str):
        rows, seat_letter = self._aircraft.get_settings_plan()
        letter = seat[-1]

        if not letter.isalpha():
            raise ValueError('you must provide a letter')

        if letter not in seat_letter:
            raise ValueError('letter must be in range')

        row = seat[:-1]

        if not row.isdigit():
            raise ValueError('row must be a digit')

        if int(row) not in rows:
            raise ValueError('row out of range')

        if self._seating[row][letter] is not None:
            raise ValueError(f'seat {seat} is already taken')

        self._seating[row][letter] = passenger_name
