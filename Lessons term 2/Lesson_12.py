class Person:
    def __init__(self, name, phone, salary=0):
        super().__init__()
        self.name = name
        self.phone = phone
        self.__salary = salary

    def get_salary(self):
        return int(self.__salary)

    def set_salary(self, salary):
        if isinstance(self, Manager):
            self.__salary = salary * 1.5
        elif isinstance(self, Developer):
            self.__salary = salary * 1
        else:
            self.__salary = salary

    def on_vacation(self, destination=None):
        self.vacation = True
        print(f'{type(self).__name__} {self.name} is now on vacation in {destination}.')

    def from_vacation(self):
        self.vacation = False
        print(f'{type(self).__name__} {self.name} back to work.')


class Preson_id:
    ID = 2

    def __init__(self):
        Preson_id.ID += 1
        self.ID = Preson_id.ID


class Manager(Person, Preson_id):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)


class Developer(Person, Preson_id):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)


m = Manager("Bob", "654321")
d = Developer("Richard", "987654")
m.set_salary(1000)
d.set_salary(1000)

print(m.__dict__, m.get_salary())
m.on_vacation()
print(m.__dict__, m.get_salary())
print(d.__dict__, d.get_salary())
m.from_vacation()
print(m.__dict__, m.get_salary())
