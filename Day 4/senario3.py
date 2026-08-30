# 3. Shopping Bill

# Ask the user for:

# Product name
# Product price
# Quantity

product_name = input("Enter Product name: ")
product_price = float(input("Enter Price of Product: "))
quantity = int(input("Enter Quantity of Product: "))

total_amount = product_price * quantity

print(total_amount)