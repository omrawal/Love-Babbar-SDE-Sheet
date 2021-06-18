# Best Time to Buy and Sell Stock


def optimal(prices):
    max_profit = 0
    n = len(prices)
    if(n < 1):
        return max_profit
    leftmin = prices[0]
    for i in range(n):
        if(prices[i] < leftmin):
            leftmin = prices[i]
        max_profit = max(max_profit, prices[i]-leftmin)
    return max_profit

# Time O(n)
# Space O(1)
