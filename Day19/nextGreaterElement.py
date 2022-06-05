class Solution:
    def nextGreaterElement(self, nums1, nums2):
        tempAns = [-1 for i in range(len(nums2))]
        ans = [-1 for i in range(len(nums1))]
        st = []
        tempAns[len(nums2)-1] = -1
        st.append(nums2[len(nums2)-1])
        for j in range(len(nums2)-2,-1,-1):
            while len(st)!=0 and nums2[j]>=st[-1]:
                st.pop()
            if len(st)==0:
                tempAns[j]=-1
            else:
                tempAns[j]=st[-1]
            st.append(nums2[j])
        for s in range(0,len(nums1),1):
            x = nums2.index(nums1[s])
            ans[s] = tempAns[x]
        return ans
        
        