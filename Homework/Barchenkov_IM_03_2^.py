# Квадратные уравнения
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
if a == 0 and b == 0 and c == 0:
    print("Корнем является любое число")
elif a == 0 and b == 0 and c == 1:
    print("Уравнение не имеет действительных корней")
elif a == 0:
    root = c / b
    print("Корень уравнения:", root)
else:
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + (discriminant**0.5)) / (2 * a)
        root2 = (-b - (discriminant**0.5)) / (2 * a)
        print("Корни уравнения:", root1, root2, "Дискриминант:", discriminant)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Корень уравнения:", root)
    else:
        print("Уравнение не имеет действительных корней")


# Задание №1
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

if b != 0:
    result = a / b
    print("Результат деления:", result)
else:
    print("Ошибка! Деление на ноль невозможно.")


# Задание №2
sum = float(input("Введите сумму покупки "))
if sum > 20:
    discount = sum * 0.35
    cost = sum - discount
    print("Стоимость:", round(cost, 2), "Скидка:", round(discount, 2))
else:
    print(
        "Сумма покупки недостаточна для получения скидки и составляет:",
        round(sum, 2),
        "y.e.",
    )


# Задание №3
num = int(input("Порядковый номер месяца: "))

if num in range(1, 13):
    months = {
        1: "Январь - Зима",
        2: "Февраль - Зима",
        3: "Март - Весна",
        4: "Апрель - Весна",
        5: "Май - Весна",
        6: "Июнь - Лето",
        7: "Июль - Лето",
        8: "Август - Лето",
        9: "Сентябрь - Осень",
        10: "Октябрь - Осень",
        11: "Ноябрь - Осень",
        12: "Декабрь - Зима",
    }
    month = months[num]
    print(month)
else:
    print("Ошибка. Нет такого месяца.")
