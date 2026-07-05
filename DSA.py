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
# count occurrence using linear search
def count_acc(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count+=1
    return count
number = [10,20,20,30,30,40]
print(count_acc(number, target = 20))