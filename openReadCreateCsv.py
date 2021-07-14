import pandas as pd # pip install pandas

# read csv file using pandas and make a dataFrame for that
df = pd.read_csv('data.csv')    # Read csv and create dataframe
numerator = df['numerator']
denominator = df['denominator']
ratio = df['ratio']
max_index = len(df.index) # to get maximum index of the dataframe
index = 0   # for index iteration in dataframe
a, b, c = [], [], []    # Create arrays to append dataframe data one by one

df2 = pd.DataFrame()    # Create an empty dataframe

# For iterating data of dataframe and append it to arrays
while index<max_index:
    a.append(numerator[index])
    b.append(denominator[index])
    c.append(ratio[index])
    index = index + 1   # for incrementing index value

# Creates columns of dataframe 2
df2['x_val'] = a
df2['y_val'] = b
df2['result'] = c
print(df2)

# upload dataframe 2 data into an csv file without index values
df2.to_csv('file_name.csv', index=False)






