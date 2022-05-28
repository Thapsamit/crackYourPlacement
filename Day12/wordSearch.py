class Solution:
    def findWord(self,i,j,row,col,board,vis,word,idx):
        if idx==len(word): 
            return True
        if i<0 or j<0 or i>=row or j>=col or vis[i][j]==True or board[i][j]!=word[idx]:
            return False
        vis[i][j] = True
        isTrue = self.findWord(i-1,j,row,col,board,vis,word,idx+1) or self.findWord(i+1,j,row,col,board,vis,word,idx+1) or self.findWord(i,j-1,row,col,board,vis,word,idx+1) or self.findWord(i,j+1,row,col,board,vis,word,idx+1)
        vis[i][j] = False
        return isTrue
        
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        vis = [[False for j in range(col)] for i in range(row)]
        idx = 0
        for i in range(0,row,1):
            for j in range(0,col,1):
                if self.findWord(i,j,row,col,board,vis,word,idx):
                    return True
        return False
            