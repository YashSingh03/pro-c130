
import pandas as pd
import csv
df = pd.read_csv("c130.csv")
print(df.columns)
print(df.shape)

del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Unnamed: 0"]
print(df.columns)
df.to_csv("main.csv")
