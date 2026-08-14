# Scenario 2: Canteen Bill 🍔
# You are developing a billing program for your college canteen.
# A student buys:
# 2 sandwiches at ₹60 each
# 1 coffee at ₹30
# 3 samosas at ₹15 each
# Calculate the total bill.
# Then make the program accept the price and quantity from the user instead of hardcoding them.
# Concepts: Variables, input, multiplication, addition.
sandwich_price = float(input("Enter the price of a sandwich: "))
sandwich_quantity = int(input("Enter the quantity of sandwiches: "))
coffee_price = float(input("Enter the price of a coffee: "))
coffee_quantity = int(input("Enter the quantity of coffees: "))
samosa_price = float(input("Enter the price of a samosa: "))
samosa_quantity = int(input("Enter the quantity of samosas: "))

sandwich = sandwich_price * sandwich_quantity
coffee = coffee_price * coffee_quantity
samosa = samosa_price * samosa_quantity

total_bill = sandwich + coffee + samosa

print("Canteen Bill")
print("Sandwiches: ", sandwich)
print("Coffee: ", coffee)
print("Samosas: ", samosa)
print("Total Bill: ", total_bill)