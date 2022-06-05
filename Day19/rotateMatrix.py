class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0,n//2,1):
            for j in range(i,n-1-i,1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
                temp = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = temp
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = temp
    
        """
        Do not return anything, modify matrix in-place instead.
        """
        