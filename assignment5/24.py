# 24. Find the smallest missing positive integer from an unsorted array.

numbers = [3, 4, -1, 1]

num_set = set(numbers)

missing = 1

while missing in num_set:
    missing += 1

print("Smallest missing positive:", missing)