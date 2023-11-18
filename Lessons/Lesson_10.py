import pandas as pd
import numpy as np
from random import randint
from matplotlib import pyplot as plt

# 1. Создать объект pandas Series из листа, объекта NumPy, и словаря

series_list = pd.Series([1, 2, 3, 4, 5])
series_numpy = pd.Series(np.array([10, 2, 30, 40, 50]))
series_dict = pd.Series({'a': 100, 'b': 200, 'c': 300})

print(f'Из листа: \n{series_list}')
print(f'Из Numpy: \n{series_numpy}')
print(f'Из словаря: \n{series_dict}')


# 2. Получить не пересекающиеся элементы в двух объектах Series

series_1 = pd.Series([randint(0, 10) for x in range(5)])
series_2 = pd.Series([randint(0, 10) for x in range(5)])
unique_1 = series_1[~series_1.isin(series_2)]
unique_2 = series_2[~series_2.isin(series_1)]

print('Уникальные в первом объекте: ', list(unique_1.values))
print('Уникальные во втором объекте: ', list(unique_2.values))


# 3. Узнать частоту уникальных элементов объекта Series (гистограмма)

series = pd.Series([randint(1, 10) for x in range(100)])
frequency = series.value_counts().sort_index()

plt.rcParams["figure.figsize"] = [10, 6]
plt.rcParams["figure.autolayout"] = True

frequency.plot.bar(color='purple')
plt.xticks(rotation=0)
plt.title('Гистограмма частоты уникальных элементов в Series')
plt.xlabel('Числа')
plt.ylabel('Частота')
plt.show()


# 4. Объединить два объекта Series вертикально и горизонтально

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([6, 7, 8, 9, 10])


vertical_concatenation = pd.concat([series1, series2], axis=0)
horizontal_concatenation = pd.concat([series1, series2], axis=1)

print(vertical_concatenation)
print(horizontal_concatenation)
print('_' * 20)

# 5. Найти разность между объектом Series и смещением объекта Series на n

n = 2
series = pd.Series([1, 5, 7, 8, 12, 15, 17])
difference = series.diff(periods=n)

print(difference)