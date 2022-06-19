class Solution:
    def findLength(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        dp = [[0 for i in range(m+1)]for j in range(n+1)]
        maxLen = 0
        for i in range(0,n+1,1):
            for j in range(0,m+1,1):
                if i==0 or j==0:
                    continue
                elif nums1[i-1]!=nums2[j-1]:
                    dp[i][j]=0
                else:
                    dp[i][j] = dp[i-1][j-1]+1
                    maxLen = max(maxLen,dp[i][j])
        return maxLen
                    
        