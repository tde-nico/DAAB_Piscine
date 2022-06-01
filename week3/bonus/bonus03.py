import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_frame = pd.read_csv("datasets/titles.csv")

raw_geners = "".join(data_frame["genres"].values)
raw_geners = raw_geners.replace("[", "")
raw_geners = raw_geners.replace("]", ",")
raw_geners = raw_geners.replace(" ", "")
raw_geners = raw_geners.replace("'", "")
genres = pd.DataFrame(raw_geners.split(","))
genres.replace('', np.nan, inplace=True)
genres.dropna(inplace=True)

genres.value_counts().plot.barh()
plt.show()


top_scores = data_frame.sort_values(by="imdb_score", ascending=False).head()
plt.bar(top_scores["title"], top_scores["imdb_score"])
plt.show()
