# Monthly Pocket Money 💰

# You receive a fixed amount of pocket money every month.

# Ask the user for:

# Monthly income
# Food expenses
# Travel expenses
# Mobile recharge
# Other expenses

# Calculate:

# Total Expenses
# Remaining Money

monthly_income = float(input("Enter your monthly income: "))
food_expenses = float(input("Enter your food expenses: "))
travel_expenses = float(input("Enter your travel expenses: "))
mobile_recharge = float(input("Enter your mobile recharge expenses: "))
other_expenses = float(input("Enter your other expenses: "))

total_expenses = food_expenses + travel_expenses + mobile_recharge + other_expenses
remaining_money = monthly_income - total_expenses

print("\nMonthly Pocket Money Summary")
print("Monthly Income:", monthly_income)
print("Food Expenses:", food_expenses)
print("Travel Expenses:", travel_expenses)
print("Mobile Recharge:", mobile_recharge)
print("Other Expenses:", other_expenses)
print("Total Expenses:", total_expenses)
print("Remaining Money:", remaining_money)