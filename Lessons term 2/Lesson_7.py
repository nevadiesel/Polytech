# Написать программу для различных математических действий над обычными дробями.
# - Реализовать проверку деления на 0 при инициации объектов.
# - Реализовать метод для вычисления точного значения дроби, округлить до 3-его знака после запятой.
# - При попытке вывода любой обычной дроби (результат вычислений или объект) сделать красивый вывод.

import re
import sympy
from fractions import Fraction


class Fraction():
    def __init__(self, num, den):
        if self.__check(den):
            self.num = num
            self.den = den
        else:
            raise ValueError('Знаменатель не может быть равен 0.')

    @staticmethod
    def __check(x):
        return False if x == 0 else True

    def value(self):
        return round(self.num / self.den, 3)

    def __str__(self):
        return str(sympy.Rational(self.num, self.den))

    def __add__(self, other):
        result_num = self.num*other.den+other.num*self.den
        result_den = self.den*other.den
        return Fraction(result_num, result_den)

    def __sub__(self, other):
        result_num = self.num*other.den-other.num*self.den
        result_den = self.den*other.den
        return Fraction(result_num, result_den)

    def __mul__(self, other):
        result_num = self.num*other.num
        result_den = self.den*other.den
        return Fraction(result_num, result_den)

    def __truediv__(self, other):
        result_num = self.num*other.den
        result_den = self.den*other.num
        return Fraction(result_num, result_den)

x = Fraction(1, 3)
y = Fraction(3, 4)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x.value())
