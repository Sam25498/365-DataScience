import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("C:/Users/sbyeg/Downloads/histogram_data.csv")

print(df_real_estate)

#For our histogram we only require one the columns which is price
plt.hist(df_real_estate["Price"])
plt.show()

#################################################################################################################
#Choosing the appropriate number of bins, or the bin size is the most crucial element of every histogram
#Through varying bin sizes a histogram can reveal vastly different insights i.e plt.hist(df_real_estate["Price"], bins = 8)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("C:/Users/sbyeg/Downloads/histogram_data.csv")

print(df_real_estate)

sns.set_style("white") #To change the backgroud of the histogram to white
plt.figure(figsize = (8, 6))
plt.hist(df_real_estate["Price"], 
         bins = 8,
        color = "108A99" )
plt.title("Distribution of Real Estate Prices", fontsize =  14, weight = "bold")
plt.xlabel("Price o (000' $)")
plt.ylabel("Number of Properties")
sns.despine() # To remove the top and right and left spine of the charts
plt.show()

