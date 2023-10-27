import os
# 2
'''
Выберите любую папку на своем компьютере, имеющую вложенные директории.
Выведите на печать в терминал ее содержимое, 
как и всех подкаталогов при помощи функции print_docs(directory).
'''


def print_docs(directory):

    for root, dirs, files in os.walk(directory):
        print(root)
        for file in files:
            print(os.path.join(root, file))


print_docs(r'/home/ivan/Documents')


# 3
'''
Требуется реализовать функцию `longest_words(file)`, 
которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько)
'''


def longest_words(file):
    f = open(file, 'r')
    text = f.read().replace('\n', ' ')
    words = text.split(' ')
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    for word in longest_words:
        print(word)
    f.close()


longest_words(r'/home/ivan/Documents/Polytech/Lessons/article.txt')


# 4
'''
Составьте программу - простейший редактор текстовых файлов.
Алгоритм работы программы:
  1. Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение `.txt`.
  2. Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки
     и переход на новую строчку.
  3. Если строка пустая или спец. символ - программа сохраняет файл.
'''


def editor():
    file_name = input("Введите имя файла: ")
    file_name += '.txt'

    lines = []
    while True:
        line = input("Введите строку: ")
        if not line or line == "/":
            break
        lines.append(line)

    file = open(file_name, 'w')
    file.write('\n'.join(lines))
    file.close()

    print("Файл сохранен.")


editor()
