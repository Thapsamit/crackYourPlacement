def findMinDiff(self, A,N,M):
    A.sort()
    minDiff = 9223372036854775807 
    for i in range(0,len(A)-M+1,1):
        minDiff = min(minDiff,A[i+M-1]-A[i])
    return minDiff