import math
from random import randint


#1
'''Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. 
Длину массива и его элементы ввести с клавиатуры. 
В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.'''


'''def replace(x):
    x[0], x[-1] = x[-1], x[0]
    return x


n = int(input("Введите длинну массива: "))
x = [randint(10, 80) for x in range(n)]

print(x)
print(replace(x))'''



#2
'''Даны две дроби A/B и C/D (A, B, C, D - натуральные числа). 
Составить программу деления дроби на дробь. Ответ должен быть несократимой дробью. 
Использовать подпрограмму алгоритма Евклида для определения НОД.'''


'''a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

a = a1 * b2
b = b1 * a2


def division(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b


a_d = a / division(a, b)
b_c = b / division(a, b)

result = a_d / b_c

print("Ответ: ", int(a_d), "/", int(b_c))'''


#3
'''Задана окружность `(x-a)^2 + (y-b)^2 = r^2` и точки P(p1, p2), F(f1, f2), L(l1, l2). 
Выяснить и вывести на экран, сколько точек и какие лежить внутри окружности. Проверку сформировать в виде процедуры.'''

'''def inside_circle(a, b, r, points):
    global inside
    inside = []

    for point in points:
        x, y = point

        distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)

        if distance < r:
            inside.append(point)
    
    return(inside)

a = 0
b = 0
r = 5
points = [(2, 3), (-1, -2), (4, 4), (-3, 0)]

inside_circle(a, b, r, points)
print(f"Внутри отружности: {len(inside)} точек.")
print(inside_circle(a, b, r, points))'''


#4
'''Даны 3 различных массива целых чисел (размер каждого не превышает 15). 
В каждом массиве найти сумму элементов и среднеарифметическое значение. Маассивы сформировать рандомно.'''

