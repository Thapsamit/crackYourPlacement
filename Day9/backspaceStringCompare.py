class Solution:
    def backspaceCompare(self, s, t):
        st = []
        tt = []
        lenS = len(s)
        lenT = len(t)
        maxLen = max(lenS,lenT)
        for i in range(0,maxLen,1):
            if i<lenS and s[i]!='#':
                st.append(s[i])
            elif i<lenS and s[i]=='#':
                if len(st)!=0:
                    st.pop()
            if i<lenT and t[i]!='#':
                tt.append(t[i])
            elif i<lenT and t[i]=='#':
                if len(tt)!=0:
                    tt.pop()
        if st==tt:
            return True
        else:
            return False
                    