import numpy as np
from matplotlib import pyplot as plt


def f1(x, a, b):
    return (x**b + a**b) / x**b


def f2(x, a, b):
    return (x**b + a**b) / x**b


def f3(x, a, b):
    return (x**b + a**b) / x**b


x = np.linspace(-4, 0, 300)

plt.plot(x, f1(x, 1, 1), color='purple', label='α = 1 \nβ = 1')
plt.plot(x, f2(x, 2, 1), color='blue', label='α = 2 \nβ = 1')
plt.plot(x, f3(x, 1, 2), color='green', label='α = 1 \nβ = 2')


x = np.linspace(0, 4, 300)

plt.plot(x, f1(x, 1, 1), color='purple')
plt.plot(x, f2(x, 2, 1), color='blue')
plt.plot(x, f3(x, 1, 2), color='green')

plt.ylim(-30, 30)
plt.xlim(-4, 4)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Задание 1')
plt.grid(True)
plt.legend()


plt.show()
