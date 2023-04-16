import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(1234)

# Define columns and their respective data types
columns = ['Monthly Income', 'Rent/Mortgage', 'Utilities', 'Transportation', 'Groceries', 'Dining Out', 'Entertainment', 'Travel', 'Clothing & Accessories', 'Health & Wellness', 'Gifts & Donations', 'Personal Care', 'Education & Training', 'Home & Garden', 'Insurance', 'Technology', 'Miscellaneous', 'Investment Type', 'Investment Name', 'Investment Amount', 'Expected Return', 'Savings Goal']
dtypes = [int]*18 + [str]*4

# Create empty dataframe with specified columns and datatypes
df = pd.DataFrame(columns=columns).astype(dict(zip(columns, dtypes)))

# Generate 60 rows of synthetic data for 5 years
for i in range(60):
    # Create new row
    row = {
        'Monthly Income': np.random.randint(4000, 6001),
        'Rent/Mortgage': np.random.randint(1000, 2001),
        'Utilities': np.random.randint(200, 301),
        'Transportation': np.random.randint(150, 251),
        'Groceries': np.random.randint(400, 601),
        'Dining Out': np.random.randint(150, 251),
        'Entertainment': np.random.randint(50, 151),
        'Travel': np.random.randint(300, 701),
        'Clothing & Accessories': np.random.randint(100, 251),
        'Health & Wellness': np.random.randint(100, 251),
        'Gifts & Donations': np.random.randint(50, 151),
        'Personal Care': np.random.randint(50, 151),
        'Education & Training': np.random.randint(300, 701),
        'Home & Garden': np.random.randint(100, 251),
        'Insurance': np.random.randint(100, 251),
        'Technology': np.random.randint(100, 251),
        'Miscellaneous': np.random.randint(50, 151),
        'Investment Type': np.random.choice(['Stocks', 'Bonds', 'Real Estate', 'Cryptocurrency']),
        'Investment Name': np.random.choice(['Apple', 'Microsoft', 'Tesla', 'Amazon', 'Vanguard', 'Blackrock', 'Goldman Sachs', 'Bitcoin', 'Ethereum']),
        'Investment Amount': np.random.randint(3000, 7001),
        'Expected Return': round(np.random.uniform(0.05, 0.15), 2),
        'Savings Goal': np.random.randint(80000, 120001)
    }
    
    # Append row to dataframe
    df = df.append(row, ignore_index=True)

# Write dataframe to csv file
df.to_csv('synthetic_data.csv', index=False)
