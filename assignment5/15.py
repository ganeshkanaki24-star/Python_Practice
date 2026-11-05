# 15. Find the Kth largest element in an unsorted array.

numbers = [3, 2, 1, 5, 6, 4]
k = 2

unique = list(set(numbers))

if k > len(unique) or k < 1:
    print("Invalid K value")
else:
    for i in range(k):
        largest = unique[0]

        for num in unique:
            if num > largest:
                largest = num

        if i == k - 1:
            print("Kth largest:", largest)

        unique.remove(largest)