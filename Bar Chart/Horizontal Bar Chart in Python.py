import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() #This overides the matplotib look, to take advantage of the seaborn styling

#Always remember to use forward "/" slashes when specifying a path to a file.
df_used_cars = pd.read_csv("C:/Users/sbyeg/Downloads/bar_chart_data.csv")

#After loading the data frame to check what it contains
df_used_cars

#to translate this data in the form of a bar chart
plt.figure(figsize = (9, 6)) #To increase the size of the plot, to make the x-axis labels readable and not overlap
plt.bar(x = df_used_cars["Cars Listings"],
        height = df_used_cars["Brand"],
       color = "midnightblue")# color = "rgbwymc" -Assigns each column an individual color

#To rotate the x-axis labes at an angle
plt.xticks(rotation = 45, fontsize = 13)
plt.yticks(fontsize = 13)
plt.title("Cars Listings by Brand", fontsize = 16, fontweight = "bold")
plt.ylabel("Number of Listings", fontsize = 13 )
plt.show()
# To save your plot as an image
plt.savefig("Used Cars Bar.png")

#Try this as well


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() #This overides the matplotib look, to take advantage of the seaborn styling

#Always remember to use forward "/" slashes when specifying a path to a file.
df_used_cars = pd.read_csv("C:/Users/sbyeg/Downloads/bar_chart_data.csv")

#After loading the data frame to check what it contains
df_used_cars

#to translate this data in the form of a bar chart
plt.figure(figsize = (9, 6)) #To increase the size of the plot, to make the x-axis labels readable and not overlap
plt.barh(df_used_cars["Brand"], df_used_cars["Cars Listings"], color = "midnightblue")# color = "rgbwymc" -Assigns each column an individual color

#To rotate the x-axis labes at an angle
plt.xticks(rotation = 45, fontsize = 13)
plt.yticks(fontsize = 13)
plt.title("Cars Listings by Brand", fontsize = 16, fontweight = "bold")
plt.ylabel("Number of Listings", fontsize = 13 )
plt.show()
# To save your plot as an image
plt.savefig("Used Cars Bar.png")
