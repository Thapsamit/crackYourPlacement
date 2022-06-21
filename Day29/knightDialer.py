class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[0 for i in range(10)] for j in range(n+1)]
        data = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[-1],[1,7,0],[2,6],[1,3],[2,4]]
        for r in range(1,n+1,1):
            for c in range(0,10,1):
                if r==1:
                    dp[r][c]=1
                else:
                    for s in data[c]:
                        if s==-1:
                            dp[r][c]=0
                        else:
                            dp[r][c]=(dp[r][c]%1000000007+dp[r-1][s]%1000000007)%1000000007
        total = 0
        
        for i in range(0,10,1):
            total=(total%1000000007+dp[n][i]%1000000007)%1000000007
        return total
