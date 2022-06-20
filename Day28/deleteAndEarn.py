class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        inclusion = 0
        exclusion = 0
        arr = [0 for i in range(max(nums)+1)]
        for s in range(0,len(nums),1):
            arr[nums[s]]+=1
        for i in range(0,len(arr),1):
            withExc = exclusion+arr[i]*i
            withInc = max(inclusion,exclusion)
            inclusion = withExc
            exclusion = withInc
        return max(inclusion,exclusion)
        