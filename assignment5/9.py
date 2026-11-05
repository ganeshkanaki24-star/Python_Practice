# 9. Rotate an array to the right by K positions.

numbers = [1, 2, 3, 4, 5]
k = 2

k = k % len(numbers)

result = numbers[-k:] + numbers[:-k] if k != 0 else numbers[:]

print("Rotated array:", result)
