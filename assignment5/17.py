# 17. Find all subarrays whose sum equals a given target.

numbers = [1, 2, 3, 4, 2, 1]
target = 6

result = []

for i in range(len(numbers)):
    total = 0

    for j in range(i, len(numbers)):
        total += numbers[j]

        if total == target:
            result.append(numbers[i:j + 1])

print("Subarrays:", result)