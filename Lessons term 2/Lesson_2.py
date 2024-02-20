class Sauce():

    def __init__(self, taste, addition=''):
        self.taste = taste
        self.addition = addition

    def show_my_sаuce(self):
        if self.addition:
            print('Соус и', self.addition)
        else:
            print('Майонез')


sauce = Sauce('сырный')
sauce.show_my_sаuce()

sauce2 = Sauce('чесночный', 'соль')
sauce2.show_my_sаuce()


class Employee():
    def __init__(self, name, age, salary, bonus=''):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

    def get_name(self):  # возвращает имя сотрудника
        print("Имя: ", self.__name)

    def get_age(self):  # возвращает возраст
        print("Возраст: ", self.__age)

    def get_salary(self):  # возвращает зарплату сотрудника
        print("Оклад: ", self.__salary)

    def set_bonus(self, bonus):  # устанавливает свойство bonus
        self.__bonus = bonus

    def get_bonus(self):  # возвращает бонус для сотрудника
        print("Бонус: ", self.__bonus)

    def get_total_salary(self):  # возвращает общую зарплату сотрудника (оклад + бонус)
        print("Общая зарплата: ", self.__salary+self.__bonus)


stas = Employee("Stas", 25, 90000)
stas.get_name()
stas.get_age()
stas.get_salary()
stas.set_bonus(5000)
stas.get_bonus()
stas.get_total_salary()


class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    # выводит список продуктов, необходимых для приготовления блюда
    def print_ingredients(self):
        print('Ингредиенты для', self.name)
        for i, ingredient in enumerate(self.ingredients, start=1):
            print(f'{i}. {ingredient}')

    def cook(self):  # сообщает название выбранного рецепта и уведомляет о готовности блюда
        print(f'Сегодня мы готовим {self.name}.')
        print(f'Выполняем инструкцию по приготовлению блюда {self.name}...')
        print(f'Блюдо {self.name} готово!')


# создаем рецепт спагетти болоньезе
spaghetti = Recipe("Спагетти болоньезе", [
                   "Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# печатаем список продуктов для рецепта спагетти
spaghetti.print_ingredients()

# готовим спагетти
spaghetti.cook()

# создаем рецепт для кекса
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар",
              "Сливочное масло", "Соль", "Ванилин"])

# печатаем рецепт кекса
cake.print_ingredients()

# готовим кекс
cake.cook()
