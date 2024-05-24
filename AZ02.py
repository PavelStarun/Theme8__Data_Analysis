import pandas as pd
from matplotlib import pyplot as plt

students = {
    'Аня': [10, 9, 10, 9, 10],
    'Боб': [8, 7, 10, 10, 7],
    'Чарли': [10, 9, 7, 7, 8],
    'Лиза': [9, 8, 9, 9, 10],
    'Настя': [8, 6, 10, 10, 9],
    'Саша': [10, 5, 10, 10, 6],
    'Сергей': [7, 6, 4, 4, 7],
    'Макс': [10, 10, 10, 10, 10],
    'Иван': [9, 9, 7, 7, 8],
    'Станислав': [3, 4, 5, 6, 7]
}

df_students = pd.DataFrame.from_dict(students, orient='index', columns=['Matematika', 'Biologia', 'Programirovanie', 'Informatika', 'Fizika'])
df_students.to_csv('студенты.csv', index_label='Имя')


df = pd.read_csv('студенты.csv')
print(df.head())

subjects = ['Matematika', 'Biologia', 'Programirovanie', 'Informatika', 'Fizika']
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