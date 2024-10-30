class Person:
    def __init__(self, name, phone, salary=0):
        self.name = name
        self.phone = phone
        self.__salary = salary
        self.is_active = True

    def get_salary(self):
        return int(self.__salary)

    def set_salary(self, salary):
        if isinstance(self, Manager):
            self.__salary = salary * 1.2
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

    @staticmethod
    def hire(name, vacancy, phone):
        if vacancy == 'manager':
            print(f'Manager {name} has been hired.')
            return Manager(name, phone)
        else:
            print(f'Developer {name} has been hired.')
            return Developer(name, phone)

    def fire(self):
        self.is_active = False
        print(f'{type(self).__name__} {self.name} has been terminated.')


class Person_id:
    ID = 2

    def __init__(self):
        Person_id.ID += 1
        self.ID = Person_id.ID


class Manager(Person, Person_id):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)


class Developer(Person, Person_id):
    def __init__(self, name, phone, salary=0):
        super().__init__(name, phone, salary)


alice = Person.hire('Alice', 'manager', '654321')
alice.set_salary(1000)
print(alice.__dict__, alice.get_salary())
alice.on_vacation("Hawaii")
print(alice.__dict__, alice.get_salary())
alice.from_vacation()
alice.fire()
print(alice.__dict__, alice.get_salary())
