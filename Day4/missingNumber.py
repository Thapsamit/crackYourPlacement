class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = (n*(n+1))//2
        sum = 0
        for i in range(0,n,1):
            sum+=nums[i]
        return total-sum