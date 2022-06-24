class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        minMoves = 0
        for i in range(len(nums)-1,0,-1):
            stand = nums[i]
            minB = nums[0]
            nums[i-1]=minMoves+nums[i-1]+(stand-minB)
            nums[0]=nums[0]+(stand-minB) 
            minMoves+=(stand-minB)
         
        print(nums)
        return minMoves
            
        