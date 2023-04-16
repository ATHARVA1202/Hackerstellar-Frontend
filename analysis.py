import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset into a Pandas dataframe
df = pd.read_csv('synthetic_data.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Savings Goal', axis=1), df['Savings Goal'], test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
