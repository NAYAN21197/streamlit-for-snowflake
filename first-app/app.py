import pandas as pd

df = pd.read_csv("data/employees.csv", header = 0 ).convert_dtypes()
print(df)


