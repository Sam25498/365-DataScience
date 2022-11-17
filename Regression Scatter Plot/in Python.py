#Method 1: makes regression scatter plot using sns.regplot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_ad_expenditure = pd.read_csv("C:/Users/sbyeg/Downloads/scatter_plot_ii.csv")
print(df_ad_expenditure)

#On this part we'll rely on the 'Seaborn' library to incorporate regression lines onto a scatter plot
#plt.figure(figsize = (10, 8))
sns.set(rc = {'figure.figsize': (9,6)})
sns.regplot(x = "Budget",
           y = "Sales",
           data = df_ad_expenditure,
           scatter_kws = {'color' : 'k'},
           line_kws = {'color': 'red'})#color = "grey"
plt.xlabel("Ad Expenditure in (000's $)")
plt.ylabel("Sales in (000's Units)")
plt.title("Effect of Ad Expediture on Sales", fontsize = 14, weight = "bold")
plt.show()

#Method 2: makes regression scatter plot using sns.lmplot

sns.lmplot(x = "Budget",
           y = "Sales",
           data = df_ad_expenditure,
           height = 10,
           scatter_kws = {'color' : 'k'},
           line_kws = {'color': 'red'})
plt.xlabel("Ad Expenditure in (000's $)")
plt.ylabel("Sales in (000's Units)")
plt.title("Effect of Ad Expediture on Sales", fontsize = 14, weight = "bold")
plt.show()
