import pandas as pd

data_frame = pd.read_csv("datasets/Salaries.csv")

print(data_frame.groupby("JobTitle").size().count())
