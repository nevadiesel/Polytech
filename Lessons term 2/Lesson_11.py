class Person:
    def __init__(self, name, phone, salary=0):
        self.name = name
        self.phone = phone
        self.__salary = salary

    def set(self, salary):
        self.__salary = salary

    def get(self):
        return int(self.__salary)


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



class Person:
    def __init__(self, name, phone, salary=0):
        self.name = name
        self.phone = phone
        self.__salary = salary

    def set(self, salary):
        # Определение класса объекта и установка salary с коэффициентом
        if isinstance(self, Managers):
            self.__salary = salary * 1.5
        elif isinstance(self, Developers):
            self.__salary = salary * 1.2
        else:
            self.__salary = salary

    def get(self):
        return int(self.__salary)

class Managers(Person):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)

class Developers(Person):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)

# Тестирование классов с различными коэффициентами для salary
x = Managers('Stas', '+7 911 1234567')
x.set(1000)
print(x.get())  # Вывод: 1500

y = Developers('Ivan', '+7 911 9876543')
y.set(1000)
print(y.get())  # Вывод: 1200
