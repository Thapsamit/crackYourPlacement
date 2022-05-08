def removeDuplicates(self, nums):
    if len(nums)==1:
        return 1
    k = -1
    for i in range(0,len(nums),1):
        if i==0:
            lp = nums[i]
        else:
            if nums[i]==lp:
                nums[i] = -1
                if k==-1:
                    k = i 
            else:
                lp = nums[i]
                if k!=-1:
                    nums[k] = nums[i]
                    nums[i] = -1
                    k+=1
    if k!=-1:
        return k
    else:
        return len(nums)