def count(self, S, m, n): 
        S.sort()
        coins = [[0 for i in range(n+1)]for j in range(m)]
        for i in range(0,m,1):
            coins[i][0]=1
            for k in range(0,n+1,1):
                if i==0:
                    if k%S[0]==0:
                        coins[i][k] = 1
                    else:
                        coins[i][k] = 0
                else:
                    if S[i]>k:
                        coins[i][k] = coins[i-1][k]
                    else:
                        coins[i][k] = coins[i-1][k]+coins[i][k-S[i]]
        return coins[m-1][n]