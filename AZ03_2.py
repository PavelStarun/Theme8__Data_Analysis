import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('sofas.csv')

average_price = df['Цена'].mean()
print(f"Средняя цена на диваны: {average_price} рублей")

plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=10, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()