# 10. Find the intersection of two arrays, including duplicate occurrences.

a = [1, 2, 2, 3, 4, 4]
b = [2, 2, 4, 4, 5]

frequency = {}

for num in a:
    frequency[num] = frequency.get(num, 0) + 1

result = []

for num in b:
    if frequency.get(num, 0) > 0:
        result.append(num)
        frequency[num] -= 1

print("Intersection:", result)