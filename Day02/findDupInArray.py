def findDuplicates(self, nums):
    ans = []
    for i in range(0,len(nums),1):
        idx = abs(nums[i])-1
        if nums[idx]<0:
            ans.append(idx+1)
        nums[idx] = -nums[idx]
    return ans