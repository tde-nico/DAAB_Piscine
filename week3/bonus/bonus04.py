import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("datasets/titles.csv")

us_movies = data_frame[data_frame["production_countries"].str.contains("US")]
year_groups = us_movies.groupby("release_year").count()["title"]
top_movies = year_groups.sort_values(ascending=False).head(20)
top_movies.plot.barh()
plt.show()
