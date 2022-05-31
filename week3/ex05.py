import pandas as pd
import numpy as np

data_frame = pd.read_csv("datasets/Salaries.csv")

max_pay = data_frame["TotalPayBenefits"].max()
print(data_frame[data_frame["TotalPayBenefits"]==max_pay]["EmployeeName"].iloc[0])
