class Person:
    def __init__(self, name, phone, salary=0):
        super().__init__()
        self.name = name
        self.phone = phone
        self.__salary = salary

    def get(self):
        return int(self.__salary)

    def set(self, salary):
        if isinstance(self, Manager):
            self.__salary = salary * 1.5
        elif isinstance(self, Developer):
            self.__salary = salary * 1
        else:
            self.__salary = salary

    def toggle_vacation(self, destination=''):
        self.on_vacation = not self.on_vacation
        return f'{type(self).__name__} {self.name} is now {"on vacation" if self.on_vacation else "back to work"} {destination}.'


class Preson_id:
    Preson_id = 2

    def __init__(self):
        Preson_id.Preson_id += 1
        self.Preson_id = Preson_id.Preson_id


class Manager(Person, Preson_id):
    def __init__(self, name, phone, salary=0, on_vacation=False):
        super().__init__(name, phone, salary)
        self.on_vacation = on_vacation


class Developer(Person, Preson_id):
    def __init__(self, name, phone, salary=0, on_vacation=False):
        super().__init__(name, phone, salary)
        self.on_vacation = on_vacation


m = Manager("Bob", "654321")
d = Developer("Richard", "987654")
m.set(1000)
d.set(1000)

print(m.toggle_vacation())
print(m.__dict__, m.get())
print(d.__dict__, d.get())
