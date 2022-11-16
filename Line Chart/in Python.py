import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()

df_spx_ftse_00_10 = pd.read_csv("C:/Users/sbyeg/Downloads/line_chart_data.csv")
print(df_spx_ftse_00_10)

df_spx_ftse_00_10["new_date"] = pd.to_datetime(df_spx_ftse_00_10["Date"]) # This transforms the date data in a format that python can work with.
df_spx_ftse_00_10


labels = ["S&P 500", "FTSE 100"]
plt.figure(figsize = (20, 8))
plt.plot(df_spx_ftse_00_10["new_date"], df_spx_ftse_00_10["GSPC500"])
plt.plot(df_spx_ftse_00_10["new_date"], df_spx_ftse_00_10["FTSE100"])
plt.ylabel("Returns")
plt.xlabel("Date")
plt.legend(labels = labels, fontsize = "large")
plt.show()


df_spx_ftse_H2_08 = df_spx_ftse_00_10[(df_spx_ftse_00_10.new_date >= '2008-07-01') &
                                      (df_spx_ftse_00_10.new_date >= '2008-12-31')]


df_spx_ftse_H2_08


