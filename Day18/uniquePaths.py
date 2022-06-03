class Solution:
    def totalPaths(self,i,j,m,n,vis,mem):
        if i<0 or j<0 or i>=m or j>=n or vis[i][j]==1:
            return 0
        if i==m-1 and j==n-1:
            return 1
        if mem[i][j]!=0:
            return mem[i][j]
        vis[i][j] = 1
        tp = self.totalPaths(i,j+1,m,n,vis,mem) + self.totalPaths(i+1,j,m,n,vis,mem)
        mem[i][j]=tp
        vis[i][j]=0
        return tp
    def uniquePaths(self, m, n):
        mem = [[0 for i in range(n+1)]for j in range(m+1)]
        vis = [[0 for i in range(n)]for j in range(m)]
        return self.totalPaths(0,0,m,n,vis,mem)
        