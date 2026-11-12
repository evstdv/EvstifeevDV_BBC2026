import pandas as pd


def pr_sep():
    print('=' * 80, end = '\n')
    

df = pd.read_csv("tested.csv")

pd.set_option('display.max_columns', None) # Для вывода таблицы со всеми столбцами
pd.set_option('display.max_rows', None)    # Для вывода таблицы со всеми строками
pd.set_option('display.width', None)       # Для вывода таблицы без переносов


n = int(input("Сколько строк таблицы вывести: "))
print("Первые", n, "строк таблицы:\n")
print(df.head(n))

pr_sep()
print("Последние 5 строк таблицы:\n")
print(df.tail(5))

pr_sep()
print("В таблице", df.shape[0], "строк и", df.shape[1], "столбцов")

pr_sep()
print("Названия всех столбцов:")
print(df.columns.tolist())

pr_sep()
print("Типы данных в столбцах:")
print(df.dtypes)

pr_sep()
names = df.columns.tolist()
print("Числовые признаки:")
for i in (5, 6, 7, 9):
    print(names[i], end = ' ')  
print("\nКатегориальные признаки:")
for i in (0, 1, 2, 3, 4, 8, 10, 11):
    print(names[i], end = ' ')
print()

pr_sep()
numerical_cols = [names[i] for i in (5, 6, 7, 9)]
result = df[numerical_cols].agg(["min", "max", "mean", "median", "std"])
print(result)

pr_sep()
pclass_col = df["Pclass"]
pclasses_count = [0, 0, 0, 0]
for pclass in pclass_col:
    pclasses_count[pclass] += 1
for i in range(1, 3 + 1):
    print(i, "класс -", pclasses_count[i], "пассажиров")

pr_sep()
my_set = set()
for x in df["Embarked"]:
    my_set.add(x)
print("Уникальных значений в Embarked:", len(my_set))

















