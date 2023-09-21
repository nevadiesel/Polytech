##### 1
a = float(input("Введите первое целое число "))
b = float(input("Введите первое целое число "))
c = float(input("Введите первое целое число "))

z = a % 1
x = b % 1
v = c % 1

if z == 0 and x == 0 and v == 0:
    if a<b:
        if a<c:
            y=a
        else:
            y=c
    else:
        if b<c:
            y=b
        else:
            y=c
    y = int(y)
    print("Минимальное число: ", y)
else:
    print("Ошибка, вводи целые!")



def check_int(num):
  try:
    int(num)
    return True
  except ValueError:
    return False 
  
a = input("Введите первое целое число ")
b = input("Введите второе целое число ")
c = input("Введите третье целое число ")

if check_int(a) and check_int(b) and check_int(c):
    if a<b:
        if a<c:
          y=a
        else:
            y=c
    else:
        if b<c:
          y=b
        else:   
         y=c
    print("Минимальное число ", y)
else:
   print("Ошибка, вводи целые!")



##### 2
def check_interval(num):
    if num >= 1 and num <= 3:
        return True
    else:
        return False

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))

numbers = [number1, number2, number3]
selected_numbers = []

for num in numbers:
    if check_interval(num):
        selected_numbers.append(num)

print("Числа, принадлежащие интервалу [1, 3]:", selected_numbers)