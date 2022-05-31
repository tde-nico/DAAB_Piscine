import pandas as pd
import numpy as np

data_frame = pd.read_csv("datasets/Salaries.csv")

min_pay = data_frame["TotalPayBenefits"].min()
print(min_pay)
print(data_frame[data_frame["TotalPayBenefits"]==min_pay]["EmployeeName"].iloc[0])
