#!/usr/bin/python3
"""module for makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0

    max_value = total + 1
    dp = [max_value] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[total] > total:
        return -1
    else:
        return dp[total]
