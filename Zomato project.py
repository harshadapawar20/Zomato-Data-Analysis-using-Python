import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read Data from CSV file
df = pd.read_csv("C:\\Users\\HARSHADA PAWAR\\OneDrive\\Desktop\\CSV files\\Zomato data .csv")
# print(df)

# Data Cleaning
def HandleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

df['rate'] = df['rate'].apply(HandleRate)
df.info()

# What type of restaurant the majority of customers order from?
sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.show()

# How many votes does each restaurant received from customer?
grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result, c='green',marker='o')
plt.xlabel("Type of restaurant",c='red',size=20)
plt.ylabel("Votes",c='red',size=20)
plt.show()

# What are the ratings that the majority of restaurants have received?
plt.hist(df['rate'],bins=5)
plt.title("Ratings Distribution")
plt.show()

# Zomato has observed most couple order most of their food online. 
# What is the average spending on each order?
couple_data = df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

# Which mode (online or offline) has recived the maximum ratings
plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate', data=df)
plt.show()

# which type of restaurant received more offline order so Zomato can provide customers with some good offer
pivot_table = df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table, annot=True,cmap='YlGnBu',fmt='d')
plt.title('Heatmap')
plt.xlabel("Online Order")
plt.ylabel("Listed In (type)")
plt.show()