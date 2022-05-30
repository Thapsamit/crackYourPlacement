def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    vis = [[0 for i in range(N+1)] for j in range(N+1)]
	    nb = [[1,2],[-1,2],[1,-2],[-1,-2],[-2,-1],[-2,1],[2,-1],[2,1]]
	    qu = []
	    qu.append([KnightPos[0],KnightPos[1],0])
	    vis[KnightPos[0]][KnightPos[1]]=1
	    while len(qu)!=0:
	        rem = qu.pop(0)
	        if rem[0]==TargetPos[0] and rem[1]==TargetPos[1]:
	            return rem[2]
	        for i in range(0,len(nb),1):
	            di = rem[0]+nb[i][0]
	            dj = rem[1]+nb[i][1]
	            if di>=1 and dj>=1 and di<=N and dj<=N and vis[di][dj]==0:
	                qu.append([di,dj,rem[2]+1])
	                vis[di][dj]=1