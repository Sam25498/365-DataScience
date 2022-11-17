import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("C:/Users/sbyeg/Downloads/scatter_data.csv")
print(df_real_estate)

plt.figure(figsize = (12,8))
plt.scatter(df_real_estate['Area (ft.)'],
            df_real_estate['Price'],
           alpha = 0.6,
            c = df_real_estate['Building Type']
           )
plt.show()
#Having a large data set might result in overplotting, to avoid this issue we can add a transparency level, "alpha": controls transparency level and takes values from 0 to 1
#in a scatter plot we can color code according to a third variable, in this way were are able to incorporate much more info in a scatter plot, e.g c = df_real_estate['Building Type']
