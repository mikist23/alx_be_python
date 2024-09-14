# Get user inputs for income and expenses
monthly_income = float(input("Enter your monthly income: ")) 
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Display the monthly savings
print(f"Your monthly savings are {monthly_savings}.")

# Calculate the projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
result = int(projected_savings)

# Display the projected savings
print(f"Projected savings after one year, with interest, is: ${result}.")