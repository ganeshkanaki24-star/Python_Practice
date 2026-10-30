# Second Largest Number
# Write a function that returns the second largest number in a list without using sort().

def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second

numbers = [10, 20, 40, 30, 50]

print("Second largest:", second_largest(numbers))