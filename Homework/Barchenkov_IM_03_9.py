import numpy as np
from matplotlib import pyplot as plt

# 2
'''
Для x>0
На том же графике сделать 2 врезки, демонстрирующие поведение графиков на 2 интервалах:
    для малых x
    для больших x
'''

plt.rcParams["figure.figsize"] = [12, 7]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    return (x**b + a**b) / x**b


x = np.linspace(0, 10, 500)

plt.plot(x, f(x, 1, 1), color='purple', label='\u03B1=1 \u03B2=1')
plt.plot(x, f(x, 2, 1), color='blue', label='\u03B1=2 \u03B2=1')
plt.plot(x, f(x, 1, 2), color='green', label='\u03B1=1 \u03B2=2')
plt.ylim(0, 30)
plt.xlim(0, 5)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Задание 2')
plt.grid(True)
plt.legend(loc='upper right')

# Для больших х
plt.subplot(3, 4, 7)
plt.plot(x, f(x, 1, 1), color='purple')
plt.plot(x, f(x, 2, 1), color='blue')
plt.plot(x, f(x, 1, 2), color='green')
plt.ylim(0.5, 1.5)
plt.xlim(7, 10)
plt.title('Для больших х')

# Для малых х
plt.subplot(3, 4, 6)
plt.plot(x, f(x, 1, 1), color='purple')
plt.plot(x, f(x, 2, 1), color='blue')
plt.plot(x, f(x, 1, 2), color='green')
plt.ylim(9, 15)
plt.xlim(0, 0.5)
plt.title('Для малых х')

plt.savefig('task2.svg')
plt.show()


# 3
'''
Для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.
'''

plt.rcParams["figure.figsize"] = [12, 7]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    return (x**b + a**b) / x**b


x = np.linspace(-20, 0, 700)

plt.plot(x, f(x, 1, 1), color='purple', label='\u03B1=1 \u03B2=1')
plt.plot(x, f(x, 2, 1), color='blue', label='\u03B1=2 \u03B2=1')
plt.plot(x, f(x, 1, 2), color='green', label='\u03B1=1 \u03B2=2')
plt.plot(x, x*0, color='black')
plt.ylim(-30, 30)
plt.xlim(-4, 0)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Задание 3')
plt.grid(True)
plt.legend(loc='upper left')

# Для x -> -∞
plt.subplot(8, 8, (11, 20))
plt.plot(x, f(x, 1, 1), color='purple')
plt.plot(x, f(x, 2, 1), color='blue')
plt.plot(x, f(x, 1, 2), color='green')
plt.plot(x, x*0, color='black')
plt.ylim(-0.5, 1.5)
plt.xlim(-10, -7)
plt.title('Для x -> -∞')

plt.savefig('task3.svg')
plt.show()


# 4
'''
Построить в общих осях графики для:
- a=1,β=0.5
- a=1,β=-0.5
- a=1,β=-1.5  
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость
______________________________________________________________________________________________________
В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с
a=1 проходят через общую точку (1, 2).

Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.

Каждый график будет содержать 4 кривые. 2 общих:
- a=1,β=0 (в качестве цвета попробуйте использовать 'b--')
- a=1,β=-1 (в качестве цвета попробуйте использовать 'r--')  
И по 2 уникальных для каждого графика:
- a=1,β=0.5 и
- a=1,β=0.8
- a=1,β=-0.5 и
- a=1,β=-0.8
- a=1,β=-1.5 и
- a=1,β=-2.5
'''


def f(x, a, β):
    return (x**β + a**β) / x**β


x = np.linspace(-10, 10, 800)

# Первая часть
plt.plot(x, f(x, 1, 0.5), 'r', label='\u03b1=1, β=0.5')
plt.plot(x, f(x, 1, -0.5), 'g', label='\u03b1=1, β=-0.5')
plt.plot(x, f(x, 1, -1.5), 'b', label='\u03b1=1, β=-1.5')
plt.ylim(-10, 30)
plt.xlim(-2, 10)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('График f(x)')
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig('task4_1.svg')
plt.show()

# Вторая часть
plt.figure(figsize=(15, 5))

# Первый график
plt.subplot(1, 3, 1)
plt.plot(x, f(x, 1, 0), 'b--', label='\u03b1=1, β=0')
plt.plot(x, f(x, 1, -1), 'r--', label='\u03b1=1, β=-1')
plt.plot(x, f(x, 1, 0.5), 'g-', label='\u03b1=1, β=0.5')
plt.plot(x, f(x, 1, 0.8), 'm-', label='\u03b1=1, β=0.8')
plt.title('График 1')
plt.ylim(0, 10)
plt.xlim(-2, 10)
plt.grid(True)
plt.legend()

# Второй график
plt.subplot(1, 3, 2)
plt.plot(x, f(x, 1, 0), 'b--', label='\u03b1=1, β=0')
plt.plot(x, f(x, 1, -1), 'r--', label='\u03b1=1, β=-1')
plt.plot(x, f(x, 1, -0.5), 'g-', label='\u03b1=1, β=-0.5')
plt.plot(x, f(x, 1, -0.8), 'm-', label='\u03b1=1, β=-0.8')
plt.title('График 2')
plt.ylim(0, 10)
plt.xlim(-2, 10)
plt.grid(True)
plt.legend()

# Третий график
plt.subplot(1, 3, 3)
plt.plot(x, f(x, 1, 0), 'b--', label='\u03b1=1, β=0')
plt.plot(x, f(x, 1, -1), 'r--', label='\u03b1=1, β=-1')
plt.plot(x, f(x, 1, -1.5), 'g-', label='\u03b1=1, β=-1.5')
plt.plot(x, f(x, 1, -2.5), 'm-', label='\u03b1=1, β=-2.5')
plt.title('График 3')
plt.ylim(0, 10)
plt.xlim(-2, 10)
plt.grid(True)
plt.legend()

plt.suptitle('Графики f(x) для a=1', fontsize=12)

#
plt.tight_layout()
plt.savefig('task4_2.svg')
plt.show()
