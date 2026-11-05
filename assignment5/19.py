# 19. Search for an element in a rotated sorted array.

numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0

left = 0
right = len(numbers) - 1

result = -1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        result = mid
        break

    if numbers[left] <= numbers[mid]:

        if numbers[left] <= target < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else:

        if numbers[mid] < target <= numbers[right]:
            left = mid + 1
        else:
            right = mid - 1

print("Element index:", result)