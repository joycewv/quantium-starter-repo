# Task 1
import dash
import pandas as pd

#Task 2

# read and extract pink morsel data from daily_sales_data files
#data0
df0 = pd.read_csv('data/daily_sales_data_0.csv')
data0 = df0[df0['product'] == 'pink morsel']
data0.to_csv('data/data_processing/pink_morsel_data0.csv', index=False)

#data1
df1 = pd.read_csv('data/daily_sales_data_1.csv')
data1 = df1[df1['product'] == 'pink morsel']
data1.to_csv('data/data_processing/pink_morsel_data1.csv', index=False)

#data2
df2 = pd.read_csv('data/daily_sales_data_2.csv')
data2 = df2[df2['product'] == 'pink morsel']
data2.to_csv('data/data_processing/pink_morsel_data2.csv', index=False)

#combine 3 pink morsel data files in 1
pink0 = pd.read_csv('data/data_processing/pink_morsel_data0.csv')
pink1 = pd.read_csv('data/data_processing/pink_morsel_data1.csv')
pink2 = pd.read_csv('data/data_processing/pink_morsel_data2.csv')
pink = [pink0, pink1, pink2]
dfp = pd.concat(pink)
dfp.to_csv('data/data_processing/pink_morsel_all.csv', index=False)

#Assigning easier to remember name
df = pd.read_csv('data/data_processing/pink_morsel_all.csv')

#Remove the $ sign from price column
df['price'] = df['price'].replace({'\$':''}, regex=True)
df.to_csv('data/data_processing/no-dollar-sign.csv', index=False)

#Ensure column price and quantity are numbers
df['price'] = df['price'].astype("float")
df['quantity'] = df['quantity'].astype("float")

#Create a new column for total sales
df['sales'] = df['price']*df['quantity']
df.to_csv('data/data_processing/total_sales_ps.csv', index=False)

#deleting product, price and quantity columns
df = df.drop(['product', 'price', 'quantity'], axis=1)
df.to_csv('data/total_sales_ps_dropped.csv', index=False)


