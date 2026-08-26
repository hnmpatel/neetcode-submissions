class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0
        for i in range(len(prices)):
            if prices[i] <= prices[buy]:
                buy = i
                continue
            if (prices[i] - prices[buy]) > profit:
                sell = i
                profit = prices[i] - prices[buy]
        return profit