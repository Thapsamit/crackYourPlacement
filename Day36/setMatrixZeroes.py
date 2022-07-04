class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        col0 = 1 
        for i in range(0,r,1):
            if matrix[i][0]==0:
                col0 = 0
            for j in range(1,c,1):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(r-1,-1,-1):
            for j in range(c-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
            if col0==0:
                matrix[i][0]=0
                    
        """
        Do not return anything, modify matrix in-place instead.
        """
        