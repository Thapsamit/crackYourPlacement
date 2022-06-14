class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        if nums[0]==0:
            return False
        maxReached = 0
        for i in range(0,n,1):
            if maxReached<i:
                return False
            maxReached = max(maxReached,i+nums[i])
        return True
        
        