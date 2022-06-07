def maxProduct(self, nums: List[int]) -> int:
        ans = -999999999
        totalProduct1 = 1
        totalProduct2 = 1
        for i in range(0,len(nums),1):
            totalProduct1*=nums[i]
            totalProduct2*=nums[len(nums)-1-i]
            ans = max(totalProduct1,ans,totalProduct2)
            if totalProduct1==0:
                totalProduct1=1
            if totalProduct2==0:
                totalProduct2=1
        return ans