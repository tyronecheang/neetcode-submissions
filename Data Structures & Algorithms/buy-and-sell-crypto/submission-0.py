class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        for i in range(len(prices)):
            for n in range(i+1, len(prices)):
                if prices[n] - prices[i] > currentMax:
                    currentMax = prices[n] - prices[i]
        return currentMax
        