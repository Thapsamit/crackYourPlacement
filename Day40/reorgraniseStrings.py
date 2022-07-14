from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dm = defaultdict(lambda:0)
        for i in s:
            dm[i]+=1
        maxHeap = [[-val,kv] for kv,val in dm.items()]
        heapq.heapify(maxHeap)
        prev = None
        ans = ""
  
        while len(maxHeap)!=0 or prev:
            if prev and not maxHeap:
                return ""
            freq,ch = heapq.heappop(maxHeap)
            ans+=ch
            freq+=1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if freq!=0:
                prev = [freq,ch]
        return ans
            
        
        
        
        