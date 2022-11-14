import pandas as pd
import matplotlib.pyplot as plt

#Always remember to use forward "/" slashes when specifying a path to a file.
df_used_cars = pd.read_csv("C:/Users/sbyeg/Downloads/bar_chart_data.csv")

#After loading the data frame to check what it contains
df_used_cars

#to translate this data in the form of a bar chart
plt.figure(figsize = (9, 6)) #To increase the size of the plot, to make the x-axis labels readable and not overlap
plt.bar(x = df_used_cars["Brand"],
        height = df_used_cars["Cars Listings"])

#To rotate the x-axis labes at an angle
plt.xticks(rotation = 45)
plt.show()
