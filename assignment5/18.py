# 18. Merge overlapping intervals in a list.

intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort(key=lambda x: x[0])

merged = []

for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval[:])
    else:
        if interval[1] > merged[-1][1]:
            merged[-1][1] = interval[1]

print("Merged intervals:", merged)