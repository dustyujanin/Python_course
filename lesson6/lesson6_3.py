class worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(worker):
    def get_fullname(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


vasya = Position('vasya', 'popov', 'director', 500, 100)
print(vasya.get_fullname())
print(vasya.get_total_income())
