# 30. Find the maximum profit from buying and selling stocks with multiple transactions.

prices = [7, 1, 5, 3, 6, 4]

profit = 0

for i in range(1, len(prices)):

    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

print("Maximum Profit:", profit)