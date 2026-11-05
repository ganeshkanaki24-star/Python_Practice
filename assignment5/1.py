# 1. Find the second-largest unique element in an array without using sort() or max().

numbers = [10, 20, 40, 30, 50, 50]

largest = float('-inf')
second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Second largest:", second)