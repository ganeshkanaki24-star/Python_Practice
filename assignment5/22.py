# 22. Find the median of two sorted arrays in O(log(m+n)) time.

def find_median(a, b):

    if len(a) > len(b):
        a, b = b, a

    m = len(a)
    n = len(b)

    left = 0
    right = m

    while left <= right:

        partition_a = (left + right) // 2
        partition_b = (m + n + 1) // 2 - partition_a

        max_left_a = float('-inf') if partition_a == 0 else a[partition_a - 1]
        min_right_a = float('inf') if partition_a == m else a[partition_a]

        max_left_b = float('-inf') if partition_b == 0 else b[partition_b - 1]
        min_right_b = float('inf') if partition_b == n else b[partition_b]

        if max_left_a <= min_right_b and max_left_b <= min_right_a:

            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) +
                        min(min_right_a, min_right_b)) / 2

            else:
                return max(max_left_a, max_left_b)

        elif max_left_a > min_right_b:
            right = partition_a - 1

        else:
            left = partition_a + 1

    return None


a = [1, 3]
b = [2]

print("Median:", find_median(a, b))