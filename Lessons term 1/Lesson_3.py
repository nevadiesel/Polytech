#Задача № 1
a = float(input("Введите стоимость одного кг. конфет"))
for i in range(11):
    print("Стоимость", i, "кг. конфет равна:", i * a)
    i += 1


#Задача №2
n = 1
a = []
while n != 0:
    n = int(input("Добавить число в последовательность: "))
    a.append(n)
s = sum(a)
l = len(a)
print("Сумма чисел:", s, "Количество чисел:", l)


# Задача №3
a = [1, '2', 3, 4, '5']
b = []

for num in a:
    number = int(num)
    b.append(number)
s = sum(b)
print(s)
