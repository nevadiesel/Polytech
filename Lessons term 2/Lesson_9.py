# Расширить задачу про дроби.
# - Добавить операции сравнения;
# - Ввести проверку хэшей: если дроби одинаковые - это один объект экземпляра класса.

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

    def __eq__(self, other):
        return sympy.Rational(self.num, self.den) == sympy.Rational(other.num, other.den)

    def __gt__(self, other):
        return sympy.Rational(self.num, self.den) > sympy.Rational(other.num, other.den)

    def __ge__(self, other):
        return sympy.Rational(self.num, self.den) >= sympy.Rational(other.num, other.den)
    
    def __hash__(self):
        return hash(sympy.Rational(self.num, self.den))
    
class Hash:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, x, y):
        return hash((x, y))
        

x = Fraction(1, 3)
y = Fraction(3, 4)

# @Hash
def equal(x, y):
    return x == y

# print('x == y: ', x == y)
# print('x > y: ', x > y)
# print('x < y: ', x < y)
# print('x >= y: ', x >= y)

print(equal(x, y))