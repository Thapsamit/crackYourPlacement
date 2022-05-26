from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        start = 0
        end = len(nums)
        curr = 0
        count = 0
        dm = defaultdict(lambda:0)
        for i in range(0,end,1):
            curr+=nums[i]
            if curr==k:
                count+=1
            if curr-k in dm:
                count+=dm[curr-k]
            dm[curr] += 1
        return count