# 28. Solve the Word Break problem using dynamic programming.

text = "leetcode"

word_list = ["leet", "code"]

n = len(text)

dp = [False] * (n + 1)

dp[0] = True

for i in range(1, n + 1):

    for j in range(i):

        if dp[j] and text[j:i] in word_list:
            dp[i] = True
            break

print("Can break the word:", dp[n])