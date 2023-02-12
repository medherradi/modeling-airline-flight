from airline import Aircraft


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
        row, letter = self.get_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f'seat {seat} is already taken')

        self._seating[row][letter] = passenger_name

    def get_seat(self, seat):
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

        return row, letter

    def rellocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self.get_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'no passenger to rellocate in {from_seat}')

        to_row, to_letter = self.get_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'the seat {to_seat} is already taken')

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def available_seat(self):
        return sum(sum(1 for place in row.values() if  place is None) 
                    for row in self._seating
                    if row is not None)
