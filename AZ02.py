import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('студенты.csv')
print(df.head())

subjects = ['Matematika', 'Biologia', 'Programirovanie', 'Informatika', 'fizika']
mean_scores = df[subjects].mean()
median_scores = df[subjects].median()

summary_df = pd.DataFrame({
    'Предмет': subjects,
    'Средняя оценка': mean_scores.values,
    'Медианная оценка': median_scores.values
})

fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=summary_df.values, colLabels=summary_df.columns, loc='center')

plt.title('Средняя и медианная оценка по каждому предмету')
plt.show()