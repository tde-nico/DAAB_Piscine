import pandas as pd
import matplotlib.pyplot as plt

#url = "https://www.stackscale.com/blog/popular-programming-languages-2021/"
#url = "https://en.wikipedia.org/wiki/List_of_Linux_distributions"
#df = df[10]
url = "https://blog.logrocket.com/web-scraping-python-lxml-pandas/"
df = pd.read_html(url)

df = df[1]

df.to_csv("test.csv")
