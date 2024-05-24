import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('smartphones.csv')

print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df['Final Price'])
print(df.loc[1111])
print(df[df['Final Price'] > 2000.00])


plt.figure(figsize=(10, 6))
plt.plot(df['Final Price'], label='Final Price')
plt.xlabel('Index')
plt.ylabel('Price')
plt.title('Цены на смартфоны')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Final Price'], bins=30, alpha=0.75)
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.title('Гистограмма цен на смартфоны')
plt.show()


company_counts = df['Brand'].value_counts()

# Построение столбчатого графика
plt.figure(figsize=(12, 8))
company_counts.plot(kind='bar')
plt.xlabel('Компания')
plt.ylabel('Количество смартфонов')
plt.title('Количество смартфонов по компаниям')
plt.xticks(rotation=45)
plt.show()