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

# plt.savefig('uwu.svg')
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


x = np.linspace(-20, 0, 500)

plt.plot(x, f(x, 1, 1), color='purple', label='\u03B1=1 \u03B2=1')
plt.plot(x, f(x, 2, 1), color='blue', label='\u03B1=2 \u03B2=1')
plt.plot(x, f(x, 1, 2), color='green', label='\u03B1=1 \u03B2=2')
plt.plot(x, x*0, color='black')


plt.ylim(-30, 30)
plt.xlim(-4, 0)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Задание 2')
plt.grid(True)
plt.legend(loc='upper left')

# Для x -> -∞
plt.subplot(5, 5, 7)
plt.plot(x, f(x, 1, 1), color='purple')
plt.plot(x, f(x, 2, 1), color='blue')
plt.plot(x, f(x, 1, 2), color='green')
plt.plot(x, x*0, color='black')
plt.ylim(-0.5, 1.5)
plt.xlim(-10, -7)
plt.title('Для x -> -∞')

# plt.savefig('uwu.svg')
plt.show()
