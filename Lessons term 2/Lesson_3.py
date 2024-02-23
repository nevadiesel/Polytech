'''
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.'''


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = self.b = self.c = 0
        if TriangleChecker.check_type(a, b, c):
            self.a = a
            self.b = b
            self.c = c
            if TriangleChecker.validate(a) and TriangleChecker.validate(b) and TriangleChecker.validate(c):
                if self.a + self.b >= self.c and self.a + self.c >= self.b and self.b + self.c >= self.a:
                    print('Ура, можно построить треугольник!')
                else:
                    print('Жаль, но из этого треугольник не сделать.')
            else:
                print('С отрицательными числами ничего не выйдет!')
        else:
            print(("Координаты должны быть числами"))

    @classmethod
    def validate(cls, arg):
        return arg > 0
    
    @classmethod
    def check_type(cls, a, b, c):
        return type(a) in (int, float) and type(b) in (int, float) and type(c) in (int, float)
    
    @staticmethod
    def calculate(side1, side2, side3):
        return side1+side2>=side3 and side2+side3>=side1 and side1+side3>=side2


triangle = TriangleChecker(3, 4, 5)
