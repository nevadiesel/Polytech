# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты.
# Чтобы закрыть доступ к переменной kg она реализовала методы set_kg() - для задания нового значения килограммов,
# get_kg() - для вывода текущего значения кг. Из-за этого возникло неудобство:
# нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов.


class KgToPounds(object):
    def __init__(self, kg):
        self.__weight = kg

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, kg):
        self.__weight = kg

    @staticmethod
    def to_pounds(value, n):
        return value * n

    def __add__(self, other):
        return self.__weight + other

    def __setattr__(self, key, value):
        if key == '_KgToPounds__weight' or key == 'note':
            return object.__setattr__(self, key, value)
        else:
            raise AttributeError("Недопустимое имя атрибута")


mass = KgToPounds(55)
print(mass.weight)
print(mass.to_pounds(mass.weight, 2.2046))

mass.note = 'масса стаса'
print(mass.note)

mass + 10
print(mass.weight)
# print(mass.__dict__)

# try:
#     mass.uwu = 1
# except AttributeError as e:
#     print(e)