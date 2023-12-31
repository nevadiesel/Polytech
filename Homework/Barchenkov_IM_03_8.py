import re
'''
Задание 3
Вовочка подготовил одно очень важное письмо, но везде указал неправильное время. 
Поэтому нужно заменить все вхождения времени на строку (TBD). Время — это строка вида 
HH:MM:SS или HH:MM, в которой HH — число от 00 до 23, а MM и SS — число от 00 до 59. 
(ВВОД: Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. 
ВЫВОД: Уважаемые! Если вы к (TBD) не вернёте чемодан, то уже в (TBD) я за себя не отвечаю. )
'''


def replace_time(text):
    time_pattern = r'\b([01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?\b'
    result = re.sub(time_pattern, '(TBD)', text)
    return result


text = "Уважаемые! Если вы к 23:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. 18:60"
print(text + '\n' + replace_time(text))
print('-' * 40)


'''
Задание 4.
Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, 
там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. Тогда он решил собрать все аббревиатуры, 
чтобы потом найти их расшифровки на http://sokr.ru/. Помогите ему. Будем считать аббревиатурой 
слова только лишь из заглавных букв (как минимум из двух). 
Если несколько таких слов разделены пробелами, то они считаются одной аббревиатурой.
'''


def find(text):
    return re.findall(r'\b[A-ZА-Я]{2,}(?: [A-ZА-Я]{2,})*\b', text)


test = 'И в первом же документе он ничего не понял,' \
        'там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п.'
print(test + '\n' + ' '.join(find(test)))
