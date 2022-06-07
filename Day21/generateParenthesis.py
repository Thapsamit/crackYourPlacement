class Solution:
    def findCombo(self,patt,op,cl,n,ans):
        if len(patt)==2*n:
            ans.append(patt)
            return 
        if op<n:
            self.findCombo(patt+'(',op+1,cl,n,ans)
        if cl<op:
            self.findCombo(patt+')',op,cl+1,n,ans)
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.findCombo('(',1,0,n,ans)
        return ans
        