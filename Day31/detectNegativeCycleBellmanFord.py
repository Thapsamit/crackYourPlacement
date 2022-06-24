class Solution:
    
	def isNegativeWeightCycle(self, n, edges):
	    dist = [999999999 for i in range(n)]
	    dist[0] = 0
	    for i in range(1,n,1):
	        for s in edges:
	            if dist[s[0]]+s[2]<dist[s[1]]:
	                dist[s[1]] = dist[s[0]]+s[2]
	    flag = 0 
	    for s in edges:
	        if dist[s[0]]+s[2]<dist[s[1]]:
	            flag=1
	            break
	    return flag