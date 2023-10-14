# Добавить проверку на возможность сущ. треугольника с введенными сторонами
import math


def s(x, y, z):
    p = (x + y + z) / 2
    s = math.sqrt(p * (p - x) * (p - y) * (p - z))
    return s


lst = list()

for i in range(1, 4):
    print('Введите стороны ', i, '-го треугольника: ')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    while a + b <= c or a + c <= b or b + c <= a:
        print('Треугольник с такими сторонами невозможен.\nВведите стороны заново.')
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
    lst.append(s(a, b, c))

for i in range(3):
    print('Площадь ', i, '-го треугольника ', lst[i])
if lst[0] == lst[1]:
    if lst[0] == lst[2]:
        print('Треугольники равновеликие')
else:
    print('Треугольники не равновеликие ')
