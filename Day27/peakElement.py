class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        start = 0 
        end = n-1
        peak = -1
        while start<=end:
            if start==0:
                if nums[start]>nums[start+1]:
                    return start
            if end==n-1:
                if nums[end]>nums[end-1]:
                    return end
            elif nums[start]>nums[start-1] and nums[start]>nums[start+1]:
                return start
            elif nums[end]>nums[end+1] and nums[end]>nums[end-1]:
                return end
            start+=1
            end-=1
        return peak
                
                
            
        