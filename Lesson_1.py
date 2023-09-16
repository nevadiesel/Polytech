import math

#№1
a = input("Ваши фамилия, имя?")
b = input("Сколько вам лет?")
c = input("Где вы живете?")
print("Ваши фамилия, имя",a)
print("Ваш возраст",b)
print("Вы живете в",c)

#№2
t = int(input())
x = int(input())
num = 9 * math.pi * t + 10 * math.cos(x)
den = math.sqrt(t) - math.fabs(math.sin(t))
mult = math.pow(math.e, x)
z = num / den * mult
print(round(z, 2))