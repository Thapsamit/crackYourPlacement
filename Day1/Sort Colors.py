def swap(self,a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
    return
def sortColors(self, nums):
    low = 0
    mid = 0
    high  = len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            self.swap(nums,mid,low)
            mid+=1
            low+=1
        elif nums[mid]==1:
            mid+=1
        else:
            self.swap(nums,mid,high)
            high-=1
    return nums