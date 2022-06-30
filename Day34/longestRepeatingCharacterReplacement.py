from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dm = defaultdict(lambda:0)
        l = 0 
        res = 0
        for r in range(0,len(s),1):
            dm[s[r]]+=1
            if (r-l+1)-max(dm.values())>k:
                dm[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res
        
        