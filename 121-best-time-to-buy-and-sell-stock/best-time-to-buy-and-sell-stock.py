class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min = prices[0]
        for i in range(1,n):
            val = prices[i]-min
            if val<=0:
                min = prices[i]
            profit = max(profit,val)

        return profit
            

