class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        profit = 0
        if n==1:
            return profit
        start = 0
        end  = 1
        while start<n-1 and end<n:
            if prices[end]-prices[start]<=0:
                start = end
                end = end+1
            else:
                profit = max(profit,prices[end]-prices[start])
                end+=1
        return profit