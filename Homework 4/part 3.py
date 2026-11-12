import pandas as pd


def pr_sep():
    print('=' * 80, end = '\n')
    

df = pd.read_csv("tested.csv")

print("Пропуски:")
print(df.isnull().sum()) # Здесь sum() - метод pandas

pr_sep()
print("Процент общего количества пропусков относительно числа строк:", df.isnull().sum().sum() / df.shape[0] * 100)

pr_sep()
print("Столбец с максимальным числом пропусков:", df.isnull().sum().idxmax())

pr_sep()
age_old_data = df["Age"].agg(["min", "max", "mean", "median", "std", "count"])


