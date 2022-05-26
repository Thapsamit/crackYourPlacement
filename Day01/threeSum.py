def threeSum(self, nums):
    nums.sort()
    ans =  []
    for i in range(0,len(nums)-2,1):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        start = i+1
        end = len(nums)-1 
        while start<end:
            currSum = nums[i]+nums[start]+nums[end]
            if currSum<0:
                start+=1
            elif currSum>0:
                end-=1
            else:
                ans.append([nums[i],nums[start],nums[end]])
                start+=1
                end-=1
                while start<end and nums[start]==nums[start-1]:
                    start+=1
                while start<end and nums[end]==nums[end+1]:
                    end-=1
    return ans