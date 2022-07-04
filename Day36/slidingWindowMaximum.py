from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        start = 0
        end = 0
        ans = []
        while end<len(nums):
            while len(dq)>0 and dq[-1]<nums[end]:
                dq.pop()
            dq.append(nums[end])
            if end-start+1<k:
                end+=1 
            elif end-start+1==k:
                ans.append(dq[0])
                if len(dq)>0 and nums[start]==dq[0]:
                    dq.popleft()
                start+=1
                end+=1
        return ans
        