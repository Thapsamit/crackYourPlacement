class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i in range(1,len(prices),1):
            if prices[i]>=prices[i-1]:
                sell+=1
            else:
                profit+=prices[sell]-prices[buy]
                buy = i
                sell = i
        profit+=prices[sell]-prices[buy]
        return profit 
        