def findDuplicate(self, nums):
    dict = {}
    for i in range(0,len(nums),1):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]]+=1
            if dict[nums[i]]>1:
                return nums[i]