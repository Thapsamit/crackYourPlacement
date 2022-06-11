import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        heapq.heapify(ans)
        for i in range(0,k,1):
            heapq.heappush(ans,nums[i])
            
        for i in range(k,len(nums),1):
            if ans[0]<nums[i]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])
        return ans[0]
        