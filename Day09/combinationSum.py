class Solution:
    def subsets(self,candidates,target,ans,idx,temp):
        if target==0:
            ans.append(temp)
            return

        for i in range(idx,len(candidates),1):
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            self.subsets(candidates,target-candidates[i],ans,i+1,temp+[candidates[i]])
    def combinationSum2(self, candidates, target):
        ans = []
        idx = 0 
        candidates.sort()
        self.subsets(candidates,target,ans,idx,[])
        return ans
        