import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


print(dalys_data.iloc[0:101:10,3:5])


my_columns=[True,False,False,True]
print(dalys_data.loc[dalys_data['Entity']=='Afghanistan',my_columns])


china_data=dalys_data.loc[dalys_data['Entity']=='China',["Entity","Year","DALYs"]]
china_data_desc=china_data.describe()
mean_china=china_data_desc.loc['mean','DALYs']
print(" Mean DALYs in China over time:",mean_china)
print(" DALYs in China in 2019:",china_data_desc.loc[china_data_desc['Year']==2019,'DALYs'].iloc[0]) #  DALYs in China in 2019 was greater than the mean


plt.plot(china_data.Year, china_data.DALYs, 'bo')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China over time")


# for qustion

data_2019=dalys_data.loc[dalys_data["Year"]==2019]
data_2019_less=data_2019.loc[data_2019['DALYs']<18000]
print("Places in the World where the DALYs in 2019 is less than 18,000 are as follows:")
print(data_2019_less["Entity"])