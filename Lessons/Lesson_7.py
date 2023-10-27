import os
# pillow
# openpyxl
n = int(input("С какой строки выводить: "))


def read_last(file, lines):
    f = open(file, 'r')
    l = [line.strip() for line in f]
    for i in range(count+1):
        if i > n:
            print(l[i-2])
    f.close()


f = open(r'/home/ivan/Documents/Polytech/Lessons/article.txt', 'r')
lst = f.read()
count = lst.count("\n") + 1

if n > 0 and n < count:
    read_last(r'/home/ivan/Documents/Polytech/Lessons/article.txt', n)
else:
    print("Развивайся, Шизик.")
