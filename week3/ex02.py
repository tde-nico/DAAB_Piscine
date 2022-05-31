import pandas as pd
import numpy as np

data_frame = pd.read_csv("datasets/Salaries.csv")

print(data_frame["OvertimePay"].max())
