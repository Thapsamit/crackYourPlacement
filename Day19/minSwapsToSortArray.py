#using graph cycle edge 

def minSwaps(self, nums):
	    arr = []
	    for i in range(0,len(nums),1):
	        arr.append([nums[i],i])
	    arr.sort()
	    vis = [False for i in range(len(nums))]
	    swaps = 0
	    for i in range(0,len(nums),1):
	        if vis[i]==True or arr[i][1]==i:
	            continue
	        cLen = 0
	        j = i
	        while vis[j]==False:
	            vis[j] = True
	            cLen+=1
	            j = arr[j][1]
	        swaps+=cLen-1
	    return swaps