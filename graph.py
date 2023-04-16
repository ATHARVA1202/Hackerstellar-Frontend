import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas dataframe
df = pd.read_csv('synthetic_data.csv')

# Create a bar chart of the total expenses by category
df.drop(['Savings Goal', 'Investment Type', 'Investment Name', 'Investment Amount', 'Expected Return'], axis=1).sum().plot(kind='bar')
plt.title('Total Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.show()

# Create a pie chart of the distribution of expenses by category
df.drop(['Savings Goal', 'Investment Type', 'Investment Name', 'Investment Amount', 'Expected Return'], axis=1).sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Expenses by Category')
plt.axis('equal')
plt.show()

# Create a scatter plot of the relationship between income and savings goal
plt.scatter(df['Monthly Income'], df['Savings Goal'])
plt.title('Income vs. Savings Goal')
plt.xlabel('Monthly Income')
plt.ylabel('Savings Goal')
plt.show()
