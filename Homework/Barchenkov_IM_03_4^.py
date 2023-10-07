# GitHub: https://github.com/nevadiesel


# 1
'''Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». 
   Преобразовать ее, заменив точками все восклицательные знаки.'''

text = 'н нфыннв!отннн нн!нннн н!н'
max_n = 0
i = 0

for n in text:
    if n == 'н':
        i += 1
        max_n = max(max_n, i)
    else:
        i = 0

print(max_n)


# 2
'''Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. 
   Вывести на экран все символы, расположенные внутри этих скобок.'''

string = "Дана строка (символов, среди которых есть) одна открывающаяся"

index_start = string.index("(") + 1
index_end = string.index(")")

print(string[index_start:index_end])


# 3
'''Дана строка. Вывести все слова, начинающиеся на букву "а"
   и слова оканчивающиеся на букву "я".'''

string = 'Дана строка. Вывести все слова, на букву "а" и зканчивается_на_я!!! Анапа'
string = string.lower()
symbols = ['.', ',', '"', '!', '?']

for i in symbols:
    string = string.replace(i, '')
words = string.split(" ")

for word in words:
    if word[0] == "а":
        print(word)
    if word[len(word) - 1] == "я":
        print(word)
