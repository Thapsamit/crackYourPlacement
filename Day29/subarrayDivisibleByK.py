from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hm = defaultdict(lambda:0)
        hm[0] = 1
        currSum = 0
        count = 0
        for i in range(0,len(nums),1):
            currSum+=nums[i]
            if currSum%k in hm:
                count+=hm[currSum%k]
            hm[currSum%k]+=1
        return count
                
        
        