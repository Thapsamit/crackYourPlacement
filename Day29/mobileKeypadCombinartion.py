class Solution:
	def getCount(self, N):
	    dp = [[0 for i in range(10)] for j in range(N+1)]
	    data = []
	    data.append([0,8])
	    data.append([1,2,4])
	    data.append([2,1,3,5])
	    data.append([3,2,6])
	    data.append([4,5,1,7])
	    data.append([5,2,4,6,8])
	    data.append([6,3,5,9])
	    data.append([7,4,8])
	    data.append([8,0,5,7,9])
	    data.append([9,6,8])
	    
	    for r in range(1,N+1,1):
	        for c in range(0,10,1):
	            if r==1:
	                dp[r][c]=1
	            else:
	                for i in data[c]:
	                    dp[r][c]+=dp[r-1][i]
	    total = 0
	    
	    for i in range(0,10,1):
	        total+=dp[N][i]
	    return total


	    [[4,6],[6,8],[7,9],[4,8],[3,9,0],[-1],[1,7,0],[2,6],[1,3],[2,4]]