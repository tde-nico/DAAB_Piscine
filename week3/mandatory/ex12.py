import pandas as pd

data_frame = pd.read_csv("datasets/Salaries.csv")

print(data_frame[data_frame["JobTitle"].str.contains("Chief")].count()["EmployeeName"])
