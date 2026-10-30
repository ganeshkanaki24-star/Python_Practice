# Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_n(n=int(input())))
