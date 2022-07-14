from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bm  = defaultdict(lambda:0)
        
        for str in strs:
            dm = [0]*26
            for i in range(0,len(str),1):
                dm[ord(str[i])-ord('a')]+=1
            if tuple(dm) not in bm:
                ans = []
                ans.append(str)
                bm[tuple(dm)] = ans
            else:
                bm[tuple(dm)].append(str)
        out = list(bm.values())
        return out
        