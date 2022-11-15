import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df_fuel_engine_type = pd.read_csv("pie_chart_data.csv")

df_fuel_engine_type

plt.figure(figsize = (10,8))
