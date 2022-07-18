class Solution:
    def find(self,par,x):
        if par[x]==x:
            return x
        temp = self.find(par,par[x])
        par[x] = temp
        return temp
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [0 for i in range(len(edges)+1)]
        rank = [0 for i in range(len(edges)+1)]
        for i in range(1,len(edges),1):
            par[i] = i;
            rank[i] = i;
        for j in range(0,len(edges),1):
            u = edges[j][0]
            v = edges[j][1]
            lu = self.find(par,u)
            lv = self.find(par,v)
            if lu!=lv:
                if rank[lu]>rank[lv]:
                    par[lv] = lu
                elif rank[lv]>rank[lu]:
                    par[lu] = lv
                else:
                    par[lu] = lv
                    rank[lv]+=1
            else:
                return edges[j]
            
        