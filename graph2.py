import matplotlib.pyplot as plt

# Accept user input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
utilities = float(input("Enter your monthly utility bills: "))

# Calculate net income and percentage breakdown
net_income = income - expenses - utilities
income_pct = income / (income + expenses + utilities) * 100
expenses_pct = expenses / (income + expenses + utilities) * 100
utilities_pct = utilities / (income + expenses + utilities) * 100
net_income_pct = net_income / (income + expenses + utilities) * 100

# Generate pie chart of income breakdown
labels = ['Income', 'Expenses', 'Utilities']
sizes = [income_pct, expenses_pct, utilities_pct]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.set_title('Monthly Income Breakdown')
plt.show()

# Generate bar chart of monthly net income
fig2, ax2 = plt.subplots()
ax2.bar(['Net Income'], [net_income])
ax2.set_title('Monthly Net Income')
plt.show()
