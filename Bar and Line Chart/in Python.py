import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df_kdnuggets = pd.read_csv("C:/Users/sbyeg/Downloads/bar_line_chart_data.csv")
print(df_kdnuggets)

fig, ax = plt.subplots(figsize = (10,7))
ax.bar(df_kdnuggets["Year"],
       df_kdnuggets["Participants"],
       color="k")
ax.set_ylabel("Number of Participants", 
              weight = "bold")
ax.tick_params(axis = "y",
               width = 2,
               labelsize = "large")
ax1 = ax.twinx()
ax1.set_ylim(0,1)
ax1.yaxis.set_major_formatter(PercentFormatter(xmax = 1.0))
ax1.plot(df_kdnuggets["Year"],
       df_kdnuggets["Python Users"],
         color = "#b60000",
         marker = "D")
