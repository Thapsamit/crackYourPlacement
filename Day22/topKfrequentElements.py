from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = defaultdict(lambda:0)
        ans = []
        out = []
        heapq.heapify(ans)
        for i in range(0,len(nums),1):
            if nums[i] not in occur:
                occur[nums[i]]=1
            else:
                occur[nums[i]]+=1
        for ke,va in occur.items():
            heapq.heappush(ans,[va,ke])
            if len(ans)>k:
                heapq.heappop(ans)
        for i in range(0,k,1):
            out.append(ans[i][1])
        return out
            
            
        