# 4. Find the missing number from an array containing numbers from 1 to N.

numbers = [1, 2, 4, 5, 6]
n = 6

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing number:", missing)