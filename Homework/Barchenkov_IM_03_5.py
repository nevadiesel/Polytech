# 1.
'''Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). 
Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, 
соединяющим начало координат с точкой, минимальный. Вычисления оформить в виде процедуры.'''
import math
from sympy import primerange
from random import randint


points = []
angles = []

for i in range(3):
    points.append([randint(-10, 10) for x in range(2)])

print(points)


def calculate_angle(x, y):
    cos = x / (math.sqrt(x**2+y**2))
    angle = math.acos(cos)
    angles.append([angle, [x, y]])


for point in points:
    x, y = point
    calculate_angle(x, y)


print(angles)
print("Координаты точки: ", min(angles)[1])
print(f"Угол: {round(min(angles)[0]*180/math.pi)} градусов.")


# 2.
'''Найти все простые натуральные числа, не превосходящие n, 
двоичная запись которых представляет собой палиндром, 
т. е. читается одинаково слева направо и справа налево.'''

n = int(input("Введите n: "))

prime = list(primerange(0, n))
polindrome_prime = []


def palindrome(num):
    number = format(num, 'b')
    if number == ''.join(reversed(number)):
        polindrome_prime.append(num)


for i in prime:
    palindrome(i)

print(prime)
print("Палиндромы в двоичной записи: ", polindrome_prime)
