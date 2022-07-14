class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        st.append(len(heights)-1)
        rb = [0 for i in range(len(heights))]
        lb = [0 for i in range(len(heights))]
        rb[len(heights)-1] = len(heights)
        for i in range(len(heights)-2,-1,-1):
            while len(st)!=0 and heights[st[-1]]>=heights[i]:
                st.pop()
            if len(st)==0:
                rb[i] = len(heights)
            else:
                rb[i] = st[-1]
            st.append(i)
        st.clear()
        st.append(0)
        lb[0] = -1
        for i in range(1,len(heights),1):
            while len(st)!=0 and heights[st[-1]]>=heights[i]:
                st.pop()
            if len(st)==0:
                lb[i] = -1
            else:
                lb[i] = st[-1]
            st.append(i)
        print(rb)
        print(lb)
        maxRec = -9999999
        for i in range(0,len(heights),1):
            width = rb[i]-lb[i]-1
            area = width * heights[i]
            if area>maxRec:
                maxRec = area
        return maxRec
        
                
        