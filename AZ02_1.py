import pandas as pd
import numpy as np


df = pd.read_csv('студенты.csv')
print(df.head())

Q1_math = df['Matematika'].quantile(0.25)
Q3_math = df['Matematika'].quantile(0.75)

IQR_math = Q3_math - Q1_math

std_math = np.std(df['Matematika'], ddof=1)

print(f"Первый квартиль: {Q1_math}")
print(f"Третий квартиль: {Q3_math}")
print(f"Межквартальный размах: {IQR_math}")
print(f"Стандартное отклонение оценок: {std_math}")
