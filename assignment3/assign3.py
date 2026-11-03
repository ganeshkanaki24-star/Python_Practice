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
# income = int(input("Enter your annual income: "))

# if income <= 250000:
#     tax = 0

# elif income <= 500000:
#     tax = (income - 250000) * 0.05

# elif income <= 1000000:
#     tax = (250000 * 0.05) + (income - 500000) * 0.20

# else:
#     tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

# print("Income Tax:", tax)

# 12 Create a menu-driven calculator using if-elif.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     print("Result:", a + b)

# elif choice == 2:
#     print("Result:", a - b)

# elif choice == 3:
#     print("Result:", a * b)

# elif choice == 4:
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Cannot divide by zero")

# else:
#     print("Invalid choice")

# 13 Print all prime numbers between 1 and n.
# n = int(input("Enter a number: "))

# for num in range(2, n + 1):
#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, end=" ")

# 14 Find the factorial of a number using a loop.
# n = int(input("Enter a number: "))

# fact = 1

# if n < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     for i in range(1, n + 1):
#         fact = fact * i

#     print("Factorial:", fact)

# 15 Print the Fibonacci series up to n terms.
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c

# 16 Check whether a number is an Armstrong number.
# num = int(input("Enter a number: "))

# temp = num
# digits = len(str(num))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** digits
#     temp //= 10

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

# 17 Reverse a number and check if it is a palindrome.
# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10

# print("Reverse:", reverse)

# if original == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome")

# 18 Find the Greatest Common Divisor (GCD) of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD:", abs(a))

# 19 Write a function to check if a string is a palindrome.
# def palindrome(text):
#     if text == text[::-1]:
#         return True
#     else:
#         return False

# word = input("Enter a word: ")

# print(palindrome(word))

# 20 Write a function to count vowels and consonants in a string.
# def count_letters(text):
#     vowels = 0
#     consonants = 0

#     for ch in text.lower():
#         if ch in "aeiou":
#             vowels += 1
#         elif ch.isalpha():
#             consonants += 1

#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

# text = input("Enter a string: ")

# count_letters(text)

# 21 Create a function to calculate simple and compound interest.
# def calculate_interest(p, r, t):
#     simple = (p * r * t) / 100

#     compound = p * (1 + r / 100) ** t - p

#     print("Simple Interest:", simple)
#     print("Compound Interest:", round(compound, 2))


# p = float(input("Enter principal amount: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time in years: "))

# calculate_interest(p, r, t)

# 22 Write a function to return all factors of a number.
# def find_factors(n):
#     factors = []

#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)

#     return factors


# num = int(input("Enter a number: "))

# if num > 0:
#     print("Factors:", find_factors(num))
# else:
#     print("Enter a positive number")

# 23 Write a function to find the second-largest number in a list.

# def second_largest(numbers):
#     largest = float('-inf')
#     second = float('-inf')

#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num

#         elif num > second and num != largest:
#             second = num

#     if second == float('-inf'):
#         return None

#     return second


# numbers = [10, 20, 40, 30, 50]

# print("Second Largest:", second_largest(numbers))

# 24 Merge two lists without duplicates.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# result = []

# for num in list1 + list2:
#     if num not in result:
#         result.append(num)

# print("Merged List:", result)

# 25 Find the second-largest and second-smallest elements.
# numbers = [10, 20, 5, 40, 30]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# if len(unique) < 2:
#     print("Not enough different elements")
# else:
#     smallest = float('inf')
#     second_smallest = float('inf')

#     largest = float('-inf')
#     second_largest = float('-inf')

#     for num in unique:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif num < second_smallest:
#             second_smallest = num

#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest:
#             second_largest = num

#     print("Second Smallest:", second_smallest)
#     print("Second Largest:", second_largest)

# 26 Rotate a list to the left by k positions.
# numbers = [1, 2, 3, 4, 5]

# k = int(input("Enter rotation: "))

# k = k % len(numbers)

# result = numbers[k:] + numbers[:k]

# print("Rotated List:", result)

# 27 Separate even and odd numbers into two lists.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even Numbers:", even)
# print("Odd Numbers:", odd)

# 28 Find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common Elements:", common)