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
           
