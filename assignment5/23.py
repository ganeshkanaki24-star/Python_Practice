# 23. Find the maximum product of a contiguous subarray.

numbers = [2, 3, -2, 4]

max_product = numbers[0]
min_product = numbers[0]
result = numbers[0]

for num in numbers[1:]:

    if num < 0:
        max_product, min_product = min_product, max_product

    max_product = max(num, max_product * num)
    min_product = min(num, min_product * num)

    result = max(result, max_product)

print("Maximum product:", result)