income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
result_monthly = int(monthly_savings)
print(f"Your monthly savings are ${result_monthly}.")

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
result = int(projected_savings)
print(f"Projected savings after one year, with interest, is: ${result}.")