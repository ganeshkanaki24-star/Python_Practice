# # 1.Find the data type of every value in a mixed
# data = [10, 20.5, "Ganesh", True, 5j, None]

# for item in data:
#     print(item, ":", type(item))


# 2  Convert a nested list into a tuple of tuples.

# numbers = [[1, 2], [3, 4], [5, 6]]

# result = tuple(tuple(item) for item in numbers)

# print(result)

# 3 Remove all duplicate values from a mixed list while preserving the original order.

# data = [10, "hello", 20, "hello", 10, 30, "python"]

# result = []

# for item in data:
#     if item not in result:
#         result.append(item)

# print(result)

# 4 Check whether a number is a power of 2 using operators.
# num = int(input("Enter a number: "))

# if num > 0 and (num & (num - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")

# 5 Swap two numbers using bitwise XOR.
# a = 10
# b = 20

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("A =", a)
# print("B =", b)

# 6 Find whether a number is divisible by both 4 and 6 using logical operators.

num = int(input("Enter a number: "))

if num % 4 == 0 and num % 6 == 0:
    print("Divisible by both 4 and 6")
else:
    print("Not divisible by both")