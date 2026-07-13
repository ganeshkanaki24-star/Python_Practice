'''
a = int(input("Enter 1 Number:"))
b = int(input("Enter 2 Number:"))
c = a + b
print("The total is:", c)
print("The Substraction:", a - b)
print("The Multiplication:", a * b)
print("the Division:", a/b)
'''
'''
# Factorial

num = int(input("Enter any Number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"Factorial of {num} is {factorial}")

'''

# Factorial from 1 to 9 

for n in range(1, 10):
    factorial = 1

    for i in range(1, n+1):
        factorial = factorial * i
    print(f"Factorial of {n} = {factorial}")