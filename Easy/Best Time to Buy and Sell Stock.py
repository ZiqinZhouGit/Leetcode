class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        i = 1
        max_profit = 0
        bottom_price = prices[0]
        while i < len(prices):
            if prices[i-1] < bottom_price:
                bottom_price = prices[i-1]
                print(bottom_price)
            profit = prices[i] - bottom_price
            if profit > max_profit:
                max_profit = profit
            i += 1
        return max_profit
