# Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".



def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(n=int(input())))