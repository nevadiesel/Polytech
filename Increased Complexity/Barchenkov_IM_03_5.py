# Привести номер к стандартному виду

import re


def normalize_phone_number(phone_number):

    formatted_number = '+7' + ' ' + \
        '(' + phone_number[1:4] + ') ' + phone_number[4:7] + \
        '-' + phone_number[7:9] + '-' + phone_number[9:11]
    return formatted_number


#text = '+7(433)625-06-40, +7 (189) 7922273 9 (911 7832267'

text = list()
while True:
    phone_number = input('Введи номер телефона: ')
    if phone_number:
        text.append(phone_number)
    else:
        break

text = str(text)


numbers = re.findall(
    r'[+]{0,1}[78][ ]*[(]{0,1}\d{3}[)]{0,1}[ ]*\d{3}[- ]*\d{2}[- ]*\d{2}', text)

if numbers:
    for numder in numbers:
        numder = re.sub('[^1234567890]', '', numder, count=0)
        print("Стандартный номер:", normalize_phone_number(numder))
else:
    print('Номера телефонов не распознаны.')
