import pandas as pd

data_frame = pd.read_csv("datasets/Salaries.csv")

counts = data_frame.groupby("JobTitle")["EmployeeName"].count()
print(counts.sort_values(ascending=False).head())
