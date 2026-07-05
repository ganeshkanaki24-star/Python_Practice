'''
# linear shearch target value
def linear_search(arr, target):
    for  i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 

nums = [10, 25, 30, 45, 50]
print(linear_search(nums, target = 25))
'''
'''
# count occurrence using linear search
def count_acc(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count+=1
    return count
number = [10,20,20,30,30,40]
print(count_acc(number, target = 20))
'''
# Binary search
def binary_search(arr, target):
    low, high = 0, len(arr) -1# start with first index (0) and last

    while low <= high:#condition until search space is valid
        mid = (low + high) // 2 #find the middle index

        # case 1 target is founded
        if arr[mid] == target:
            return mid
        # case 2 target is rater than middle value
        elif arr[mid]<target:
            low = mid + 1# ignore left search in right side
        # case 3 target value is less that middle 
        else:
            high = mid - 1#ignore right side and search left side 
    return -1 # ignore not found

arr = [1,2,3,4,5,6,7,8,9]
target = 9
print(binary_search(arr, target))
           
# sorting 

arr = [7,3,5,2,1,8]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted:", arr)

# dictionary of product prices
shop_price = {
    "Shoes": 250,
    "Shirt": 100,
    "Cap": 75,
    "watch": 300,
    "jeans": 150
}

# sort products by price using bubble sort
items = list(shop_price.items())

for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_shop_price = dict(items)
print(sorted_shop_price)

