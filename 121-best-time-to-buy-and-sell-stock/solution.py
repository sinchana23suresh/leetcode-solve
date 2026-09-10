// 53 ms | 19.3 MB
class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > profit:
                profit = prices[i] - lowest

        return profit