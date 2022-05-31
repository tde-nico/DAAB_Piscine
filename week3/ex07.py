import pandas as pd
import numpy as np

data_frame = pd.read_csv("datasets/Salaries.csv")

print(data_frame[data_frame["Year"]==2011]["BasePay"].mean())
print(data_frame[data_frame["Year"]==2012]["BasePay"].mean())
print(data_frame[data_frame["Year"]==2013]["BasePay"].mean())
print(data_frame[data_frame["Year"]==2014]["BasePay"].mean())
