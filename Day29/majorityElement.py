import math
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        count = 1
        lowerLimit = math.floor(len(nums)/2)
        for i in range(1,len(nums),1):
            if nums[i]==nums[i-1]:
                count+=1
                if count>lowerLimit:
                    return nums[i]
            else:
                count=1
       