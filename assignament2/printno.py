# Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print(print_numbers(n=int(input())))