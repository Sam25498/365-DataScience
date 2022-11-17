import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#Method 1: Using matplotlib.pyplot to create a scatter plot
df_real_estate = pd.read_csv("C:/Users/sbyeg/Downloads/scatter_data.csv")
print(df_real_estate)

plt.figure(figsize = (12,8))
scatter = plt.scatter(df_real_estate['Area (ft.)'],
            df_real_estate['Price'],
           alpha = 0.6,
            c = df_real_estate['Building Type'],
            cmap = 'viridis')
plt.legend(*scatter.legend_elements(),
          loc = "upper left",
          title = "Building Type")
plt.title("Relationship between Area and Price of California Real Estate", fontsize = 14, weight = "bold")
plt.xlabel("Area (sq. ft)", wight = "bold")
plt.ylabel("Price (000's of $)")
plt.show()
#Having a large data set might result in overplotting, to avoid this issue we can add a transparency level, "alpha": controls transparency level and takes values from 0 to 1
#in a scatter plot we can color code according to a third variable, in this way were are able to incorporate much more info in a scatter plot, e.g c = df_real_estate['Building Type']
#Briefly with the pointer we are specifying the location in the memory where the first element of the array element is.

#Method 2: Making Use of Seaborn to create a scatter plot 
plt.figure(figsize = (12,8))
sns.scatterplot(df_real_estate["Price"],
                df_real_estate["Area (ft.)"],
                hue = df_real_estate['Building Type'],
                palette = ['black', 'darkblue', 'purple', 'pink', 'white'],
                s = 100)
plt.title("Relationship between Area and Price of California Real Estate", fontsize = 14, weight = "bold")
plt.xlabel("Area (sq. ft)", wight = "bold")
plt.ylabel("Price (000's of $)")
plt.show()
