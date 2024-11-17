import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.1 Создание Series из списка
data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print("Series из списка:")
print(series_from_list)

# 1.2 Создание Series из NumPy массива
data_array = np.array([10, 20, 30, 40, 50])
series_from_array = pd.Series(data_array)
print("Series из NumPy массива:")
print(series_from_array)

# 1.3 Создание DataFrame из словаря
data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df_from_dict = pd.DataFrame(data_dict)
print("DataFrame из словаря:")
print(df_from_dict)

# 2.1
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

# Не пересекающиеся элементы (симметрическая разность)
unique_ser1 = series1[~series1.isin(series2)]
unique_ser2 = series2[~series2.isin(series1)]

print("Элементы, не пересекающиеся с series_2:")
print(unique_ser1)
print("Элементы, не пересекающиеся с series_1:")
print(unique_ser2)
# 2.2
df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [3, 4, 5, 6]
})

unique_col1 = df['col1'][~df['col1'].isin(df['col2'])]
unique_col2 = df['col2'][~df['col2'].isin(df['col1'])]
print("Не пересекающиеся элементы в столбце 'col1':")
print(unique_col1)
print("Не пересекающиеся элементы в столбце 'col2':")
print(unique_col2)

# 3
data_series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
frequency = data_series.value_counts()
print("Частота уникальных элементов в Series:")
print(frequency)
plt.bar(frequency.index, frequency.values)
plt.xlabel('Элементы')
plt.ylabel('Частота')
plt.title('Гистограмма частоты уникальных элементов')
plt.show()

# 4
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
df_vertical = pd.concat([df1, df2], ignore_index=True)

print("Вертикальная конкатенация:")
print(df_vertical)

df_horizontal = pd.concat([df1, df2], axis=1)
print("Горизонтальная конкатенация:")
print(df_horizontal)

# 5
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y1': np.sin(np.linspace(0, 10, 100)),
    'y2': np.cos(np.linspace(0, 10, 100)),
})
plt.plot(df['x'], df['y1'], label='sin(x)')
plt.plot(df['x'], df['y2'], label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики sin(x) и cos(x)')
plt.grid()
plt.legend()
plt.show()
