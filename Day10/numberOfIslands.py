class Solution:
    def getConnectedComponents(self,grid,visited,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0" or visited[i][j]==True:
            return 
        visited[i][j] = True
        self.getConnectedComponents(grid,visited,i-1,j)
        self.getConnectedComponents(grid,visited,i,j+1)
        self.getConnectedComponents(grid,visited,i+1,j)
        self.getConnectedComponents(grid,visited,i,j-1)
        
    def numIslands(self, grid:):
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(0,len(grid),1):
            for j in range(0,len(grid[0]),1):
                if grid[i][j]=="1" and visited[i][j]==False:
                    self.getConnectedComponents(grid,visited,i,j)
                    count+=1
        return count 