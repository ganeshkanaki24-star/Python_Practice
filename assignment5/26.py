# 26. Find the longest increasing subsequence in an array.

numbers = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [1] * len(numbers)

previous = [-1] * len(numbers)

for i in range(len(numbers)):

    for j in range(i):

        if numbers[j] < numbers[i]:

            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                previous[i] = j

length = max(dp)

index = dp.index(length)

result = []

while index != -1:
    result.append(numbers[index])
    index = previous[index]

result.reverse()

print("Longest Increasing Subsequence:", result)
print("Length:", length)