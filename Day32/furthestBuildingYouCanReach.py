import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        heapq.heapify(arr)
        for i in range(0,len(heights)-1,1):
            jump = heights[i+1]-heights[i]
            if jump>0:
                heapq.heappush(arr,jump)
            if len(arr)>ladders:
                bricks-=heapq.heappop(arr)
            if bricks<0:
                return i 
        return len(heights)-1
            
        