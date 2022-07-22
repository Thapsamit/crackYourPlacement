class Solution:
    def liveNeighbours(self,i,j,r,c,board):
        neigh = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
        count = 0
        for q in neigh:
            newR = i+q[0]
            newC = j+q[1]
            if newR>=0 and newR<r and newC>=0 and newC<c:
                if board[newR][newC] in [1,3]:
                    count+=1
        return count
            
            
            
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        # orig   new    state
        #  0      0       0
        #  1      0       1
        #  0      1       2
        #  1      1       3
        
        r = len(board)
        c = len(board[0])
        for i in range(0,r,1):
            for j in range(0,c,1):
                totalLiveNeighbours = self.liveNeighbours(i,j,r,c,board)
                if board[i][j]==1:
                    if totalLiveNeighbours in [2,3]:
                        board[i][j] = 3
                else:
                    if totalLiveNeighbours==3:
                        board[i][j] = 2
                    
        for i in range(0,r,1):
            for j in range(0,c,1):
                if board[i][j]==1:
                    board[i][j]=0
                elif board[i][j] in [2,3]:
                    board[i][j] = 1
            
                
        """
        Do not return anything, modify board in-place instead.
        """
        