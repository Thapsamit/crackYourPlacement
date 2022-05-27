class Solution:
    def ratMaze(self,maze,row,col,rd,cd,ans,paths):
        if row<0 or col<0 or row>=rd or col>=cd or maze[row][col]==0:
            return
        if row==rd-1 and col==cd-1:
            paths.append(ans)
            return
        maze[row][col] = 0
        self.ratMaze(maze,row+1,col,rd,cd,ans+"D",paths)
        self.ratMaze(maze,row,col+1,rd,cd,ans+"R",paths)
        self.ratMaze(maze,row-1,col,rd,cd,ans+"U",paths)
        self.ratMaze(maze,row,col-1,rd,cd,ans+"L",paths)
       
        maze[row][col] = 1

        return paths
    def findPath(self, m, n):
        paths = []
        self.ratMaze(m,0,0,n,n,"",paths)
       
        return paths