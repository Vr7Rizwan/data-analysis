import pandas as pd

data = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(data)

data = {
    'Name':["John","Anna","Peter"],
    "Age":[28,24,35],
    "Country":["USA","UK","USA"]
}
df = pd.DataFrame(data);
print(df);
print(df.head(2)) # To get first 2 values
print(df.tail(2)) # To get last 2 values
df.info() # To display all information about the DataFrame
print(df.dtypes) # To get data type
print(df.shape) # To get number of rows and columms
print(df.describe()) # To get statistical summary of the DataFrame
print(df.sort_values(by='Age').reset_index(drop=True)) # To sort the DataFrame by Age column and reset the index
print(df.query("Age >= 30")) # To filter rows where Age is greater than or equal to 30
print(df.groupby('Country')["Age"].mean()) # To group the DataFrame by Country and calculate the mean Age for each group
print(df["Country"].unique()) # To get unique values in the Country column
print(df["Country"].nunique()) # To get the number of unique values in the Country column