import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv('dz.csv')

df['City'] = df['City'].fillna('Томск')
df['Salary'] = df.groupby('City')['Salary'].transform(lambda x: x.fillna(x.mean()))
print(df)

city_salary_mean = df.groupby('City')['Salary'].mean()

plt.figure(figsize=(12, 8))
city_salary_mean.plot(kind='bar')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')
plt.title('Средняя зарплата по городам')
plt.xticks(rotation=45)
plt.show()




