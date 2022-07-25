from collections import defaultdict
class Solution:
    def onesZeroes(self,str):
        dm = defaultdict(lambda:0)
        for i in range(0,len(str),1):
            dm[str[i]]+=1
        return dm
    def largestSubset(self,strs,m,n,mem,idx):
        if idx==len(strs) or m+n==0:
            return 0 
        if mem[m][n][idx]!=-1:
            return mem[m][n][idx]
        
        dm = self.onesZeroes(strs[idx])
        include = 0
        if m>=dm["0"] and n>=dm["1"]:
            include = 1+self.largestSubset(strs,m-dm["0"],n-dm["1"],mem,idx+1)
        exclude = self.largestSubset(strs,m,n,mem,idx+1)
        mem[m][n][idx] = max(include,exclude)
        return mem[m][n][idx]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = [[[-1 for i in range(len(strs))]for j in range(n+1)]for k in range(m+1)]
        return self.largestSubset(strs,m,n,mem,0)
        