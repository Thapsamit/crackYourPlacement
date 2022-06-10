class Solution:
    def lengthOfLIS(self, nums):
        dp = [0 for i in range(len(nums))]
        dp[0] = 1 
        for j in range(1,len(nums),1):
            maxLCS = 0
            for idx in range(0,j,1):
                if nums[j]>nums[idx]:
                    maxLCS = max(maxLCS,dp[idx])
            dp[j] = maxLCS+1
    
        return max(dp)