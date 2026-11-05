# 25. Count the number of subarrays whose sum equals K.

numbers = [1, 2, 3, -2, 2]
k = 3

frequency = {0: 1}

current_sum = 0
count = 0

for num in numbers:

    current_sum += num

    count += frequency.get(current_sum - k, 0)

    frequency[current_sum] = frequency.get(current_sum, 0) + 1

print("Number of subarrays:", count)