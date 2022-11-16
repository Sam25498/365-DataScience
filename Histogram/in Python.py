import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("C:/Users/sbyeg/Downloads/histogram_data.csv")

print(df_real_estate)

#For our histogram we only require one the columns which is price
plt.hist(df_real_estate["Price"])
plt.show()

#Choosing the appropriate number of bins, or the bin size is the most crucial element of every histogram
#Through varying bin sizes a histogram can reveal vastly different insights


