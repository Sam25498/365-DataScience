import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_fuel_engine_types = pd.read_csv("stacked_area_chart_data.csv")

print(df_fuel_engine_types)

colors = ["011638", "#7e2987", "#ef2026"]
plt.figure(figsize = (12, 6))
plt.stackplot(df_fuel_engine_types["Year"],
              df_fuel_engine_types["Diesel"],
              df_fuel_engine_types["Petrol"],
              df_fuel_engine_types["Gas"],
             colors = colors,
             edgecolor = 'none') #'edgecolor' helps control the border colors
plt.xticks(df_fuel_engine_types["Year"], rotation = 45)
plt.show()
