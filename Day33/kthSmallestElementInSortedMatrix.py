import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        heapq.heapify(arr)
        count = 0
        for i in range(0,len(matrix),1):
            for j in range(0,len(matrix[0]),1):
                heapq.heappush(arr,-1*matrix[i][j])
                count+=1
                if count==k:
                    r = i
                    c = j
                    break
            if count==k:
                break
        print(arr)
        for i in range(r,len(matrix),1):
            for j in range(0,len(matrix[0]),1):
                if (r==i and j==c) or (r==i and j<c):
                    continue
                if arr[0]<(-1*matrix[i][j]):
                    heapq.heappop(arr)
                    heapq.heappush(arr,-1*matrix[i][j])
        return -1*arr[0]
        