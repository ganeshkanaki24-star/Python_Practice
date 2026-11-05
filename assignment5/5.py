# 5. Find all duplicate elements in a list without using nested loops.

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))