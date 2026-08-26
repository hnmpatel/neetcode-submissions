class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        profit = 0
        tmp_profit = 0
        buy = 0
        for i in range(len(prices)):
            if prices[i] <= prices[buy] or prices[i] < prices[i-1]:
                buy = i
            else:
                if (prices[i] - prices[buy]) > tmp_profit:
                    tmp_profit = prices[i] - prices[buy]
                if prices[i] > prices[i+1]:
                    profit += tmp_profit
                    tmp_profit = 0
            
        return profit