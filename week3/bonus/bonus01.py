import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("datasets/titles.csv")

plt.plot(data_frame.groupby("release_year").size())
plt.show()
