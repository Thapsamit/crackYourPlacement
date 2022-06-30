class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i in range(0,len(temperatures),1):
            while len(st)!=0 and temperatures[i]>st[-1][0]:
                stE,stI = st[-1]
                st.pop()
                res[stI] = i-stI
            st.append([temperatures[i],i])
        return res
                
        