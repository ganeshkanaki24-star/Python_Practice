# 2. Find all pairs in an array whose sum equals a given target.

numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs:", pairs)