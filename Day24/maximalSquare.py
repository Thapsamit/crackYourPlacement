class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]=="1":
                    if i==m-1:
                        dp[i][j] = int(matrix[i][j])
                    elif j==n-1:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])+1
        
        maxSquare = 0
        for i in range(0,m,1):
            for j in range(0,n,1):
                print(maxSquare)
                maxSquare = max(maxSquare,dp[i][j])
        return maxSquare*maxSquare