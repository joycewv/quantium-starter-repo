# Task 1
import dash
import pandas as pd

#Task 2

# read and extract pink morsel data from daily_sales_data files
#data0
df0 = pd.read_csv('data/daily_sales_data_0.csv')
data0 = df0[df0['product'] == 'pink morsel']
data0.to_csv('data/pink_morsel_data0.csv', index=False)

#data1
df1 = pd.read_csv('data/daily_sales_data_1.csv')
data1 = df1[df1['product'] == 'pink morsel']
data1.to_csv('data/pink_morsel_data1.csv', index=False)

#data2
df2 = pd.read_csv('data/daily_sales_data_2.csv')
data2 = df2[df2['product'] == 'pink morsel']
data2.to_csv('data/pink_morsel_data2.csv', index=False)

#combine 3 pink morsel data files in 1
pink0 = pd.read_csv('data/pink_morsel_data0.csv')
pink1 = pd.read_csv('data/pink_morsel_data1.csv')
pink2 = pd.read_csv('data/pink_morsel_data2.csv')
pink = [pink0, pink1, pink2]
dfp = pd.concat(pink)
dfp.to_csv('data/pink_morsel_all.csv', index=False)

#Calculate Sales Data
df = pd.read_csv('data/pink_morsel_all.csv')
dfs = df.assign(sales=lambda x: x.price.split('$') * x.quantity)
print(dfs)
#dfs = df.assign(sales=)

#def SalesData():
    #data0['sales'] =