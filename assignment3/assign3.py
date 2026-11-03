# # 1.Find the data type of every value in a mixed
# data = [10, 20.5, "Ganesh", True, 5j, None]

# for item in data:
#     print(item, ":", type(item))


# 2  Convert a nested list into a tuple of tuples.

# numbers = [[1, 2], [3, 4], [5, 6]]

# result = tuple(tuple(item) for item in numbers)

# print(result)

# 3 Remove all duplicate values from a mixed list while preserving the original order.

data = [10, "hello", 20, "hello", 10, 30, "python"]

result = []

for item in data:
    if item not in result:
        result.append(item)

print(result)