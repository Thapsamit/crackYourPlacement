def histogram(self,his):
        lb = [0 for i in range(len(his))]
        rb = [0 for i in range(len(his))]
        st = []
        st.append(len(his)-1)
        rb[len(his)-1] = len(his)
        for i in range(len(his)-2,-1,-1):
            while len(st)!=0 and his[st[-1]]>=his[i]:
                st.pop()
            if len(st)==0:
                rb[i] = len(his)
            else:
                rb[i] = st[-1]
            st.append(i)
        st.clear()
        st.append(0)
        lb[0] = -1 
        for i in range(1,len(his),1):
            while len(st)!=0 and his[st[-1]]>=his[i]:
                st.pop()
            if len(st)==0:
                lb[i] = -1
            else:
                lb[i] = st[-1]
            st.append(i)
        maxArea = -999999
        for i in range(0,len(his),1):
            dis = rb[i]-lb[i]-1
            area = dis*his[i]
            if maxArea<area:
                maxArea = area
        return maxArea
                
    def maxArea(self,M, n, m):
        his = []
        maxRec = -9999999
        for i in range(0,m,1):
            his.append(M[0][i])
        maxRec = max(maxRec,self.histogram(his))
        for i in range(1,n,1):
            for j in range(0,m,1):
                if M[i][j]==0:
                    his[j] = 0
                else:
                    his[j] = his[j]+1
            maxRec = max(maxRec,self.histogram(his))
        return maxRec