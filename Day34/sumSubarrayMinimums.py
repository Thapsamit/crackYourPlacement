class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = [0]
        arr = [0]+arr
        res = [0]*len(arr)
        for i in range(0,len(arr),1):
            while len(st)!=0 and arr[st[-1]]>arr[i]:
                st.pop()
            j = st[-1]
            res[i] = res[j]+(i-j)*arr[i]
            st.append(i)
        return sum(res)%(10**9+7)