# Вывод алфавита
result = []
for c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    result.append("|" + c.upper() + c + "|")
print(20*'-')
for i in range(0, len(result), 5):
    print(''.join(result[i:i+5]), "\n" + "-"*20)


# Рамочка
m, n, i = int(input("Горизонталь: ")), int(input("Вертикаль: ")), 0
if m > 0 and n > 0:
    space = (m - 2) * " "
    print(m*"@")
    for i in range(n - 2):
        print(f"@{space}@")
    print(m*"@") if n != 1 else 0
else:
    print("Error.")


# Задание №1
lim = int(input("Верхний предел: "))
if lim <= 100:
    summa = 0
    num = 1
    while num <= lim:
        summa += num ** 3
        num += 1
    print(summa)
else:
    print("Ошибка! Вводи число не больше 100.")


# Задание №2
for i in range(1, 10):
    for j in range(1, 10):
        print("%4d" % (i * j), end="")
    print()
