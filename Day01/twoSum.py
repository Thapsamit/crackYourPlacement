def twoSum(self, nums, target):
    hMap = {}
    ans = []
    for i in range(0,len(nums),1):
        curr = target-nums[i]
        if curr in hMap:
            ans.append(hMap[curr])
            ans.append(i)
            break
        hMap[nums[i]] = i
    return ans