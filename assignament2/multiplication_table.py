# Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
table(num)
