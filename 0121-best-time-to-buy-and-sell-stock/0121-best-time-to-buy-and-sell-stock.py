class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max1 = 0
        min_price = prices[0]
        for i in range(1,n):
            profit = prices[i] - min_price
            if profit > max1:
                max1 = profit
            elif prices[i] < min_price:
                min_price = prices[i]
        return max1            