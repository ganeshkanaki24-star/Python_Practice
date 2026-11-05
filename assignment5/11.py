# 11. Find the maximum sum of a contiguous subarray.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = numbers[0]
maximum_sum = numbers[0]

for i in range(1, len(numbers)):
    current_sum = max(numbers[i], current_sum + numbers[i])

    maximum_sum = max(maximum_sum, current_sum)

print("Maximum subarray sum:", maximum_sum)