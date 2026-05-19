import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing the file we are gonna use

df = pd.read_csv(
    r"C:\Users\ASUS\Downloads\Global_Superstore2.csv\Global_Superstore2.csv" ,
    encoding = 'ISO-8859-1'
    )

# Checking the data 

print(df.head())
print(df.info())
print(df.isnull().sum())

# Remove Duplicate values

df.drop_duplicates(inplace = True) 

#Fill missing values in text columns

object_columns = df.select_dtypes(include=['object', 'string']).columns
df[object_columns] = df[object_columns].fillna('Unknown')

#Fill missing values in numeric columns

numerics_col = df.select_dtypes(include=np.number).columns
df[numerics_col] = df[numerics_col].fillna(0)

# Clean column names

df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

#Convert Date Column

df['order_date'] = pd.to_datetime(df['order_date'], dayfirst = True ,errors = 'coerce')
df['months'] = df['order_date'].dt.month_name()

# ------------------------------
# Data Analysis
# ------------------------------

# Total Sales

print(df['sales'].sum())

# Top Selling Categories

print(df.groupby('category')['sales'].sum().sort_values(ascending=False))

# Monthly Sales Trend

print(df.groupby(df['order_date'].dt.month)['sales'].sum())

# Highest Sales Cities

print(df.groupby('city')['sales'].sum().sort_values(ascending=False).head(10))

# Most Profitable Categories

print(df.groupby('category')['profit'].sum())

# Which Categories Have Losses?

print(df.groupby('category')['profit'].sum().sort_values())

# ------------------------------
# Visualizations
# ------------------------------

# Graph 1: Sales by Category
plt.figure(figsize = (10,6))
df.groupby('category')['sales'].sum().plot(kind = 'bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()

# Graph 2: Monthly Sales Trend
plt.figure(figsize=(8,5))
df.groupby(df['order_date'].dt.month)['sales'].sum().plot(kind='line')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()

# Graph 3: Top 10 Cities by Sales
plt.figure(figsize=(10,6))

df.groupby('city')['sales'].sum().sort_values(ascending = False).head(10).plot(kind='bar')

plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.show()

# Graph 4: Profit by Category
plt.figure(figsize=(8,5))

sns.barplot(
    x = df.groupby('category')['profit'].sum().index,
    y = df.groupby('category')['profit'].sum().values
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.show()

# Graph 5: Discount vs Profit
plt.figure(figsize = (10,8))
plt.scatter(df['discount'], df['profit'])

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.show()

# Graph 6: Correlation Heatmap

sns.heatmap(df.corr(numeric_only = True) , annot = True , cmap = 'coolwarm')

plt.title("Correlation Heatmap")

plt.show()