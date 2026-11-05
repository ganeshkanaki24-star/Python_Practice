# 29. Find the minimum number of jumps required to reach the last index.

numbers = [2, 3, 1, 1, 4]

jumps = 0
current_end = 0
farthest = 0

for i in range(len(numbers) - 1):

    farthest = max(farthest, i + numbers[i])

    if i == current_end:

        if farthest == current_end:
            jumps = -1
            break

        jumps += 1
        current_end = farthest

print("Minimum jumps:", jumps)