#Вывод алфавита
result = []
for c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    result.append("|"+c.upper()+c+"|")
print(20*'-')
for i in range(0, len(result), 5):
    print(''.join(result[i:i+5]), "\n" + "-"*20)


# Задание №1
lim = int(input("Верхний предел: "))
summa = 0
num = 1
while num <= lim:
    summa += num ** 3
    num += 1
print(summa)


# Задание №2
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i * j)
    print("-" * 10)
