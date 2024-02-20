import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Посчитать среднюю доходность женщин

file = '../Mall_Customers.csv'
df = pd.DataFrame()
df = pd.read_csv(file)
df = df.set_index('Genre')
df = df.groupby(level='Genre').mean()

print('Cредняя доходность женщин:', df.iloc[0]['Annual Income (k$)'])


# 2. Определить у обеих полов людей с бОльшими расходами;

df = pd.read_csv(file)
df = df.set_index('Genre')
df = df.groupby(level='Genre').max()

print('ID Женщины с макс доходом:', df.iloc[0]['CustomerID'])
print('ID Мужчины с макс доходом:', df.iloc[1]['CustomerID'])


# 3. Построить график зависимости доходов от возраста для мужчин;

df = pd.read_csv(file)
df = df[df['Genre'] == 'Male']

plt.rcParams["figure.autolayout"] = True
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Annual Income (k$)'], color='blue')
plt.title('Зависимость доходов от возраста для мужчин')
plt.xlabel('Возраст')
plt.ylabel('Годовой доход (тыс. $)')
plt.grid(True)
plt.tight_layout()
plt.legend()
# plt.show()


# 4. Построить столбчатый график для мужчин одним цветом, для женщин другим,
#       отображающий распрделение расходов в зависимости от доходов.

df = pd.read_csv(file)
female_data = df[df['Genre'] == 'Female']
male_data = df[df['Genre'] == 'Male']


plt.figure(figsize=(12, 6))

plt.bar(male_data['Annual Income (k$)'], male_data['Spending Score (1-100)'],
        width=0.4, align='edge', label='Мужчины', color='blue')
plt.bar(female_data['Annual Income (k$)'] - 0.4, female_data['Spending Score (1-100)'],
        width=0.4, align='edge', label='Женщины', color='pink')
plt.xlabel('Годовой доход (тыс. $)')
plt.ylabel('Средний балл расходов (1-100)')
plt.title('Средний балл расходов по полу и годовому доходу')
plt.legend()
plt.show()
