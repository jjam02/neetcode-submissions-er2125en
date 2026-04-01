class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0
        for right in range(len(prices)):
            profit = prices[right]-prices[left]
            if prices[left]>prices[right]:
                left = right
            if best < profit:
                best = profit
        return best