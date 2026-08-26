class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        profit = 0
        tmp_profit = 0
        buy = 0
        in_transaction = False
        for i in range(len(prices)):
            if prices[i] <= prices[buy] or not in_transaction:
                buy = i
                in_transaction = True
                continue
            if (prices[i] - prices[buy]) > tmp_profit:
                tmp_profit = prices[i] - prices[buy]
            if prices[i] > prices[i+1]:
                profit += tmp_profit
                tmp_profit = 0
                in_transaction = False
            
        return profit