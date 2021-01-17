# ==============================
#         Information
# ==============================

# Title: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Language: Python

# Example
    # Input:
    # prices = [7,1,5,3,6,4]
    # Output:
    # 5
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# ==============================
#         Solution
# ==============================


def get_max_profit(prices):
    buy_index = 0
    sell_index = 1
    max_profit = 0

    while sell_index < len(prices):
        if prices[buy_index] < prices[sell_index]:
            profit = prices[sell_index] - prices[buy_index]
            max_profit = max(max_profit, profit)
        else:
            buy_index = sell_index
        sell_index += 1
    
    return max_profit



prices = [7, 1, 5, 3, 6, 4]

print(get_max_profit(prices))
