# Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.


def largest(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input())
b = int(input())
print(largest(a, b))