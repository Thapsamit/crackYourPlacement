class Solution:
    def spiralOrder(self, matrix):
        tRows = len(matrix)
        tCols = len(matrix[0])
        maxR = tRows-1
        maxC = tCols-1
        ans = []
        
        minc = 0
        minr = 0
        tEle = tRows*tCols
        count = 0
        while count<tEle:
            i = minr
            j = minc
            while j<=maxC and count<tEle:
                ans.append(matrix[i][j])
                j+=1
                count+=1
            minr+=1
            i = minr
            j = maxC
            while i<=maxR and count<tEle:
                ans.append(matrix[i][j])
                i+=1
                count+=1
            maxC-=1
            i = maxR
            j = maxC
            while j>=minc and count<tEle:
                ans.append(matrix[i][j])
                j-=1
                count+=1
            maxR-=1
            i = maxR
            j = minc
            while i>=minr and count<tEle:
                ans.append(matrix[i][j])
                count+=1
                i-=1
            minc+=1
        
            
        return ans
        