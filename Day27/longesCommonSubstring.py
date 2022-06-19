class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        maxLen = 0
        for i in range(0,n+1,1):
            for j in range(0,m+1,1):
                if i==0 or j==0:
                    dp[i][j]=0
                else:
                    c1 = S1[i-1]
                    c2 = S2[j-1]
                    if c1!=c2:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                        maxLen = max(maxLen,dp[i][j])
                        
        return maxLen