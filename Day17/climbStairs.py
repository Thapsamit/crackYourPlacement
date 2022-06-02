class Solution:
    def climb(self,n,x,qb):
        if x>n:
            return 0
        if x==n:
            return 1
        if qb[x]!=0:
            return qb[x]
        n1 = self.climb(n,x+1,qb)
        n2 = self.climb(n,x+2,qb)
        bothSum = n1+n2
        qb[x] = bothSum
        return bothSum
        
    def climbStairs(self, n):
        x = 0
        qb = [0 for i in range(n+1)]
        tp = self.climb(n,x,qb)
        return tp