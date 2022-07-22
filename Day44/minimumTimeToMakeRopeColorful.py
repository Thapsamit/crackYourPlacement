import heapq
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors)==1:
            return 0
        arr = [neededTime[0]]
        price = 0
        heapq.heapify(arr)
        for i in range(1,len(colors),1):
            if colors[i]==colors[i-1]:
                heapq.heappush(arr,neededTime[i])
                price+=arr[0]
                heapq.heappop(arr)
            else:
                heapq.heappop(arr)
                heapq.heappush(arr,neededTime[i])
        return price
        