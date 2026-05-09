import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing the file we are gonna use

df = pd.read_csv(r"C:\Users\ASUS\Downloads\netflix_titles.csv.zip")

# Check for null values

df.isnull().sum()

# Fill missing values

df['director'].fillna('Unknown', inplace = True)
df['country'].fillna('Unknown', inplace = True)

# Remove Duplicate values

df.drop_duplicates(inplace = True)

#Convert Date Column

df['date_added'] = pd.to_datetime(df['date_added'], errors = 'coerce')

# How many Movies vs TV Shows?

print(df['type'].value_counts())

# Which year had the most content added?

print(df['date_added'].dt.year.value_counts())

# Top 10 countries producing Netflix content

print(df['country'].value_counts().head(10))

# Most common ratings (TV-MA, PG, etc.)

print(df['rating'].value_counts())

# Most common genres

print(df['listed_in'].value_counts())

## GRAPHS

# Graph 1: Movies vs TV Shows

plt.figure(figsize=(8,5))

sns.countplot(x = 'type', data = df)

plt.title('Movies vs TV Shows')

plt.show()

# Graph 2: Content Added by Year

plt.figure(figsize=(8,5))

df['date_added'].dt.year.value_counts().sort_index().plot(kind='line')

plt.title("Content added over years")

plt.show()

# Graph 3: Top 10 Countries

plt.figure(figsize=(8,5))

df['country'].value_counts().head(10).plot(kind='bar')

plt.title("Countries making content")

plt.show()

# Graph 4: Heatmap

plt.figure(figsize=(8,5))

sns.heatmap(df.corr(numeric_only=True), annot = True)

plt.show()