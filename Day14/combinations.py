class Solution:
    def combination(self,nRange,i,n,k,ans,com):
        if k==0:
            ans.append(com) 
            return
        for j in range(i,len(nRange),1):
            self.combination(nRange,j+1,n,k-1,ans,com+[nRange[j]])
            
    def combine(self, n, k):
        ans = []
        nRange = [i for i in range(1,n+1,1)]
        self.combination(nRange,0,n,k,ans,[])
        return ans
        