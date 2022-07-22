class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0 or len(prices)==1 or k==0:
            return 0
        dp = [[0 for i in range(len(prices))] for j in range(k+1)]
        totalMax = -99999999
        for r in range(1,k+1,1):
            maxOfDiagonal = -9999999
            for c in range(1,len(prices),1):
                if dp[r-1][c-1] - prices[c-1] > maxOfDiagonal:
                    maxOfDiagonal = dp[r-1][c-1] - prices[c-1]
                if maxOfDiagonal+prices[c]>dp[r][c-1]:
                    dp[r][c] = maxOfDiagonal+prices[c]
                else:
                    dp[r][c] = dp[r][c-1]
                
                
                if c==len(prices)-1:
                    currMax = dp[r][c]
                    if currMax>totalMax:
                        totalMax = currMax
        return totalMax
                
        