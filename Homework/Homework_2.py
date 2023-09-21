#Задание №1
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

if b != 0:
    result = a / b
    print("Результат деления:", result)
else:
    print("Ошибка! Деление на ноль невозможно.")

#Задание №2
sum = float(input("Введите сумму покупки \n"))
if sum > 20:
  discount = sum * 0.35
  cost = sum - discount
  print("Стоимость:", round(cost, 2),"Скидка:", round(discount, 2))
else:
  print("Сумма покупки недостаточна для получения скидки и составляет:", round(sum, 2), "y.e.")

#Задание №3
a = int(input())
if a == 12 or a == 1 or a == 2:
  b = "Зима."
  if a == 12:
    print("Декабрь,", b)
  elif a == 1:
    print("Январь,", b)
  else:
    print("Февраль,", b)
elif a in range(3,6):
  b = "Весна."
  if a == 3:
    print("Март,", b)
  elif a == 4:
    print("Апрель,", b)
  else:
    print("Май,", b)
elif a in range(6, 9):
  b = "Лето."
  if a == 6:
    print("Март,", b)
  elif a == 7:
    print("Апрель,", b)
  else:
    print("Май,", b)
elif a in range(9, 12):
  b = "Осень."
  if a == 9:
    print("Сентябрь,", b)
  elif a == 10:
    print("Октябрь,", b)
  else:
    print("Ноябрь,", b)
else:
  print("Error, Нет такого месяца")