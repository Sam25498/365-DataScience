import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df_kdnuggets = pd.read_csv("C:/Users/sbyeg/Downloads/bar_line_chart_data.csv")
print(df_kdnuggets)

fig, ax = plt.subplots(figsize = (10,7))
ax.bar(df_kdnuggets["Year"],
       df_kdnuggets["Participants"],
       color="k")
ax1 = ax.twinx()

ax1.plot(df_kdnuggets["Year"],
       df_kdnuggets["Python Users"],
         color = "#b60000",
         marker = "D")
