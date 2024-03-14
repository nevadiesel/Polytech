# Написать программу для вычисления производной и построения графика от показательной функции.
import math
import numpy as np
from matplotlib import pyplot as plt


class Derivate:
    def __init__(self, func):
        self.func = func

    def __call__(self, x, a, dx=0.0001):
        return (self.func(x + dx, a) - self.func(x, a)) / dx


class Plot:
    def __init__(self, func):
        self.func = func

    def __call__(self, x, a):
        x = np.linspace(-1, 3, 100)
        y = self.func(x, a)
        plt.plot(x, y)
        plt.grid(True)
        plt.show()


@Plot
@Derivate
def func(x, a):
    return math.e ** (x ** a)

def sin(x):
    return math.sin(x)

func(1, 2)
