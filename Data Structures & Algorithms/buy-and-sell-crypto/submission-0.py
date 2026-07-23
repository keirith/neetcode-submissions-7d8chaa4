class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 #initalize pointers
        sell = 1
        max_profit = 0 #default case

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        
        return max_profit



        

        