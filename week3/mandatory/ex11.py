import pandas as pd

data_frame = pd.read_csv("datasets/Salaries.csv")

counts = data_frame[data_frame["Year"]==2013].groupby("JobTitle")["EmployeeName"].count()
print(counts[counts==1].value_counts().iloc[0])
