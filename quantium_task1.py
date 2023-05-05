# Task 1
import dash
import pandas as pd

#Task 2

# read data from daily_sales_data files

df0 = pd.read_csv('data/daily_sales_data_0.csv')
data0 = df0[df0['product'] == 'pink morsel']
#print(data0)

df1 = pd.read_csv('data/daily_sales_data_1.csv')
data1 = df1[df1['product'] == 'pink morsel']
#print(data1)

df2 = pd.read_csv('data/daily_sales_data_2.csv')
data2 = df2[df2['product'] == 'pink morsel']
#print(data2)





#df = pd.read_csv('daily_sales_data_1.csv')
#df = pd.read_csv('daily_sales_data_2.csv')