import numpy as np
import matplotlib.pyplot as plt


mean = 0      # Среднее значение
std_dev = 1   # Стандартное отклонение
num_samples = 1000  # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Гистограмма случайных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()


num_samples = 1000
x_data = np.random.rand(num_samples)
y_data = np.random.rand(num_samples)
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.5)
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('x ось')
plt.ylabel('y ось')
plt.grid(True)
plt.show()