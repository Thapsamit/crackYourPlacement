class Solution:
    def maxArea(self, height):
        totalWater = 0
        start = 0
        end = len(height)-1
        while start<end:
            totalWater = max(totalWater,min(height[start],height[end])*(end-start))
            if height[start]<height[end]:
                start+=1
            elif height[start]>height[end]:
                end-=1
            else:
                start+=1
                end-=1
        return totalWater