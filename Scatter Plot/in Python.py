import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df_real_estate = pd.read_csv("C:/Users/sbyeg/Downloads/scatter_data.csv")
print(df_real_estate)

plt.figure(figsize = (12,8))
plt.scatter(df_real_estate['Area (ft.)'],
            df_real_estate['Price'])
plt.show()

