# 1
'''Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива;
максимальное значение среди элементов второй строки массива. Вывести полученные значения.'''
from random import randint

'''
n = 3
arr = list()

for i in range(n):
    brr = list()
    for j in range(n):
        brr.append(randint(0, 9))
    arr.append(brr)


max_arr = max(arr[i][2] for i in range(3))
max_in_str = max(arr[2][j] for j in range(3))

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()


print(max_arr)
print(max_in_str)'''


# 2
'''Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, 
а отрицательные нулями. Вывести оба массива.'''

n = 3
m = 3
arr = list()

for i in range(n):
    brr = list()
    for j in range(m):
        brr.append(randint(-9, 9))
    arr.append(brr)


for i in range(n):
    for j in range(m):
        print("%2d" % arr[i][j], end=' ')
    print()


new_arr = [[0] * m] * n

for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            new_arr[i][j] = 1


print()

for i in range(n):
    for j in range(m):
        print("%2d" % new_arr[i][j], end=' ')
    print()

#3
'''Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, 
т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.'''




