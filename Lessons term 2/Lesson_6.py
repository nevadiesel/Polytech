# Написать программу для вычисления производной и построения графика от показательной функции.
import math
import numpy as np
from matplotlib import pyplot as plt


class Derivate:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, x, dx=0.0001):
        return (self.func(a, x + dx) - self.func(a, x)) / dx


class Plot:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, x):
        x = np.linspace(-1, 3, 100)
        y = self.func(a, x)
        plt.plot(x, y)
        plt.grid(True)
        plt.show()


# @Plot
@Derivate
@Plot
def func(a, x):
    return math.e ** (a ** x)

def sin(x):
    return math.sin(x)

print(func(1, 3))
