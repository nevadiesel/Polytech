class Person:
    def __init__(self, name, phone, salary=0):
        self.name = name
        self.phone = phone
        self.__salary = salary

    def get(self):
        return int(self.__salary)

    def set(self, salary):
        if isinstance(self, Managers):
            self.__salary = salary * 1.5
        elif isinstance(self, Developers):
            self.__salary = salary * 1
        else:
            self.__salary = salary


class Managers(Person):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)

class Developers(Person):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)

x = Managers('Stas', '+7 911 1234567')
x.set(1000)
print(x.get())

y = Developers('Ivan', '+7 911 9876543')
y.set(1000)
print(y.get())


'''class Person:
    def __init__(self, name, phone, salary=0):
        self.name = name
        self.phone = phone
        self.__salary = salary

    def get(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary


class Manager(Person):
    def __init__(self, name, phone):
        super().__init__(name, phone)

    def set_salary(self, new_salary):
        super().set_salary(new_salary)


class Developer(Person):
    def __init__(self, name, phone):
        super().__init__(name, phone)

    def set_salary(self, new_salary):
        super().set_salary(int(new_salary * 1.2))


m = Manager("Bob", "654321")
d = Developer("Charlie", "987654")
m.set_salary(1000)
d.set_salary(1000)

print(m.get())
print(d.get())
'''