class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,price in enumerate(prices):
            buy = min(prices[:i+1])
            profit = max(price-buy,profit)
        return profit

