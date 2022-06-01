import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("datasets/titles.csv")

movie_count = data_frame[data_frame["type"]=="MOVIE"].count()["title"]
show_cuont = data_frame[data_frame["type"]=="SHOW"].count()["title"]

plt.bar(["Movies", "Shows"], [movie_count, show_cuont])
plt.show()
