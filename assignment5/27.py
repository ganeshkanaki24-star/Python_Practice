# 27. Solve the Coin Change problem using dynamic programming.

coins = [1, 2, 5]
amount = 11

dp = [float('inf')] * (amount + 1)

dp[0] = 0

for coin in coins:

    for i in range(coin, amount + 1):

        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Change is not possible")
else:
    print("Minimum coins required:", dp[amount])