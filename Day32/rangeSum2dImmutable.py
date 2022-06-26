class NumMatrix:

    def __init__(self, matrix):
        Rows = len(matrix)
        Cols = len(matrix[0])
        self.sumMat = [[0 for i in range(Cols+1)] for j in range(Rows+1)]
        for r in range(0,Rows,1):
            prefix = 0
            for c in range(0,Cols,1):
                prefix+=matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix+above
    def sumRegion(self, row1, col1, row2, col2):
        
        # plus one because in sumMat we have one more row and one column
        row1 = row1+1
        col1 = col1+1
        row2 = row2+1
        col2 = col2+1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1-1][col2]
        left = self.sumMat[row2][col1-1]
        topLeft = self.sumMat[row1-1][col1-1]
        return bottomRight-above-left+topLeft
         
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)