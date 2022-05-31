class Solution:
    def maxDistance(self, grid):
        m = len(grid)
        n = len(grid[0])
        totalCell = m*n
        qu = []
        for i in range(0,m,1):
            for j in range(0,n,1):
                if grid[i][j]==1:
                    qu.append([i,j])
        if len(qu)==totalCell or len(qu)==0:
            return -1
        nb = [[-1,0],[1,0],[0,1],[0,-1]]
        level = -1
        while len(qu)!=0:
            level+=1
            si = len(qu)
            for k in range(0,si,1):
                rem = qu.pop(0)
                for s in range(0,len(nb),1):
                    di = rem[0]+nb[s][0]
                    dj = rem[1]+nb[s][1]
                    if di>=0 and dj>=0 and di<m and dj<n and grid[di][dj]==0:
                        qu.append([di,dj])
                        grid[di][dj]=1
        return level    
                
        