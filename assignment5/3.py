# 3. Move all zeros to the end of an array without changing the order of other elements.

numbers = [0, 1, 0, 3, 12, 0, 5]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

zero_count = len(numbers) - len(result)

result.extend([0] * zero_count)

print("Result:", result)