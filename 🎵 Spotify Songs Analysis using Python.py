import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing the file we are gonna use

df = pd.read_csv(r"C:\Users\ASUS\Downloads\dataset.csv\dataset.csv")

# Remove Duplicate values

df.drop_duplicates(inplace = True)

# Fill missing values

df.fillna("Unknown")

# Clean column names

df.columns = df.columns.str.strip().str.lower()

# ------------------------------
# Data Analysis
# ------------------------------

# Top 10 artists

a = df['artists'].value_counts().head(10)
print(a)

# Most popular songs

b = df.sort_values(by = 'popularity' , ascending = False)
print(b)

# Explicit vs Non-explicit songs

c = df['explicit'].value_counts()
print(c)

# Average danceability

d = df['danceability'].mean()
print(d)

# Correlation matrix

e = df.corr(numeric_only=True)
print(e)

# ------------------------------
# Visualizations
# ------------------------------

# Graph 1: Top Artists
plt.figure(figsize = "10,6")
df['artists'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Artists")
plt.xlabel("Artists")
plt.ylabel("Number of Songs")

plt.show()

# Graph 2: Popularity Distribution
plt.figure(figsize=(8,5))

sns.histplot(df['popularity'])

plt.title('Song Analisys on the basis of popularity')
plt.xlabel("Popularity")

plt.show()

# Graph 3: Explicit vs Non-Explicit Songs
plt.figure(figsize=(6,4))

sns.countplot(x = 'explicit' , data = df)

plt.title('Explicit vs Non-Explicit Songs')

plt.show()

# Graph 4: Correlation Heatmap
plt.figure(figsize=(10,8))

sns.heatmap(df.corr(numeric_only=True), annot = True)

plt.title('Correlation Heatmap')

plt.show()

# Graph 5: Danceability vs Popularity
plt.figure(figsize=(8,5))

plt.scatter(df['danceability'] , df['popularity'])

plt.xlabel('Danceability')
plt.ylabel('Popularity')

plt.title("Danceability vs Popularity")

plt.show()