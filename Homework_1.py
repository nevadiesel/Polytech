import math

# №1
r = float(input('Введите радиус: '))
a = 2 * math.pi * r
print(round(a, 2))

# №2
x = 10
y = 55
print(x,y)
x, y = y, x
print(x, y)

# №3
g = 9.81
l = int(input("Введите длинну маятника: "))
t = 2 * math.pi * math.sqrt(l/g)
print(round(t, 2))