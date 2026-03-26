class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        min = prices[0]
        profit = 0
        for i in range(1,n):
            if prices[i]<min:
                min=prices[i]
            else:
                profit += prices[i]-min
                min = prices[i]
        return profit
        