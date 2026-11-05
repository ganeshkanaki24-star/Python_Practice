# 20. Find the longest consecutive sequence in an unsorted array.

numbers = [100, 4, 200, 1, 3, 2]

num_set = set(numbers)

longest = 0

for num in num_set:
    if num - 1 not in num_set:
        current = num
        count = 1

        while current + 1 in num_set:
            current += 1
            count += 1

        if count > longest:
            longest = count

print("Longest consecutive sequence length:", longest)
