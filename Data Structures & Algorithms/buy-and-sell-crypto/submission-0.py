class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = 1000
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest  = prices[i]
            if prices[i] > cheapest:
                if ((prices[i] - cheapest) > max_profit):
                    max_profit = prices[i] - cheapest
        return max_profit


 