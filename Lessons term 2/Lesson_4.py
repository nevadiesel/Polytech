'''Простой класс, представляющий рациональную дробь (num – числитель, den – знаменатель).
Класс содержит конструктор и методы умножения и деления (дроби на дробь и дроби на целое число). 
Метод создания случайной дроби из заданного диапазона целых чисел объявлен как статический. 
Следует отметить, что в языке имеется готовый тип Fraction в модуле fractions. 
И данный пример нужно рассматривать только как образец для создания собственных классов.'''
import re
from fractions import Fraction

class Fraction():
    def __init__(self, num, den):
        if self.__check(den):
            self.__num = num
            self.__den = den
        else:
            raise ValueError('Знаменатель не может быть равен 0.')

    @staticmethod
    def __check(den):
        return False if den == 0 else True

    def _get_data(self):
        return self.__num, self.__den

    def set_num_den(self, num, den):
        self.__num = num
        self.__den = den

    def multiplication(self, a, b=1):
        result_num = self.__num * a
        result_den = self.__den * b
        print(result_num, '/', result_den)

    def division(self, a, b=1):
        result_num = self.__num * b
        result_den = self.__den * a
        print(result_num, '/', result_den)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("Недопустимое имя атрибута")
        else:
            return object.__setattr__(self, key, value)


fraction = Fraction(1, 2)
# fraction.z = 10
print(fraction._get_data())
fraction.multiplication(3, 8)
fraction.division(2)
