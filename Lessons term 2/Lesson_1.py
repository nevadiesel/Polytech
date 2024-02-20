import re


class Cats:
    age = 1
    color = 'white'

    def set_eyes_color(self, eyes_color):
        self.eyes_color = eyes_color

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


mio = Cats()
mio.color = 'brown'
mio.set_eyes_color('blue')
mio.set_phone_number('+79618062512')
print(mio.phone_number)
print()

check = re.fullmatch(
    r'[+]{0,1}[78][ ]*[(]{0,1}\d{3}[)]{0,1}[ ]*\d{3}[- ]*\d{2}[- ]*\d{2}', mio.phone_number)
if check:
    print('Correct phone number')
else:
    print('Wrong phone number')