class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self._registration

    def get_model(self):
        return self._model

    def get_settings_plan(self):
        return (range(1, self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])
