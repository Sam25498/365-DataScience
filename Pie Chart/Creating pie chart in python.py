import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df_fuel_engine_type = pd.read_csv("pie_chart_data.csv")

df_fuel_engine_type

plt.figure(figsize = (10,8))
plt.pie(df_fuel_engine_type['Number of Cars'],
        labels = df_fuel_engine_type['Engine Fuel Type'].values,
        autopct = '%.2f%%',
        textprops = {'size' : 'x-large',
                     'fontweight' : 'bold',
                    'rotation' : '30'})
       
plt.show()

