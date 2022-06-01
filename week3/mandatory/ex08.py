import pandas as pd

data_frame = pd.read_csv("datasets/Salaries.csv")

print(data_frame[2014>=data_frame["Year"]][data_frame["Year"]>=2011].groupby("Year")["BasePay"].mean())
