class Person:
    def __init__(self, name, phone, salary=0):
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


class Manager(Person):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)

class Developer(Person):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)

m = Manager("Bob", "654321")
d = Developer("Richard", "987654")
m.set(1000)
d.set(1000)

print(m.get())
print(d.get())

