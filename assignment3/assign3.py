# # 1.Find the data type of every value in a mixed
# data = [10, 20.5, "Ganesh", True, 5j, None]

# for item in data:
#     print(item, ":", type(item))


# 2  Convert a nested list into a tuple of tuples.

# numbers = [[1, 2], [3, 4], [5, 6]]

# result = tuple(tuple(item) for item in numbers)

# print(result)

# 3 Remove all duplicate values from a mixed list while preserving the original order.

# data = [10, "hello", 20, "hello", 10, 30, "python"]

# result = []

# for item in data:
#     if item not in result:
#         result.append(item)

# print(result)

# 4 Check whether a number is a power of 2 using operators.
# num = int(input("Enter a number: "))

# if num > 0 and (num & (num - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")

# 5 Swap two numbers using bitwise XOR.
# a = 10
# b = 20

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("A =", a)
# print("B =", b)

# 6 Find whether a number is divisible by both 4 and 6 using logical operators.

# num = int(input("Enter a number: "))

# if num % 4 == 0 and num % 6 == 0:
#     print("Divisible by both 4 and 6")
# else:
#     print("Not divisible by both")

# 7 Calculate the total electricity bill using different unit rates.

# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 2

# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3

# else:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5

# print("Total Electricity Bill: Rs.", bill)

# 8 Check whether three sides can form a triangle.
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Valid Triangle")
# else:
#     print("Not a Valid Triangle")

# 9 Determine the type of triangle (Equilateral, Isosceles, Scalene).
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:

#     if a == b == c:
#         print("Equilateral Triangle")

#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")

#     else:
#         print("Scalene Triangle")

# else:
#     print("Invalid Triangle")

# 10 Create a simple ATM menu (Withdraw, Deposit, Balance).

# balance = 5000

# while True:
#     print("\n1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         amount = int(input("Enter withdrawal amount: "))

#         if amount > 0 and amount <= balance:
#             balance -= amount
#             print("Withdrawal successful")
#         else:
#             print("Insufficient balance or invalid amount")

#     elif choice == 2:
#         amount = int(input("Enter deposit amount: "))

#         if amount > 0:
#             balance += amount
#             print("Deposit successful")
#         else:
#             print("Invalid amount")

#     elif choice == 3:
#         print("Available Balance:", balance)

#     elif choice == 4:
#         print("Thank you for using ATM")
#         break

#     else:
#         print("Invalid choice")

# 11 Calculate income tax based on different tax slabs.
income = int(input("Enter your annual income: "))

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Income Tax:", tax)