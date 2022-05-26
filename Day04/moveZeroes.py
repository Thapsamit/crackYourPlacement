class Solution(object):
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def moveZeroes(self, nums):
        zero = -1
        for i in range(0,len(nums),1):
            if nums[i]==0 and zero==-1:
                zero = i
            elif nums[i]!=0:
                if zero!=-1:
                    self.swap(nums,i,zero)
                    zero+=1
        return nums