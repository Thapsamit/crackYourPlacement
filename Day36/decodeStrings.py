class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(0,len(s),1):
            if s[i]!=']':
                st.append(s[i])
            else:
                encStr = ""
                while st[-1]!='[':
                    encStr = st.pop()+encStr
                st.pop()
                dig = ''
                while len(st)>0 and st[-1]>='0' and st[-1]<='9':
                    dig = st.pop()+dig
                st.append(int(dig)*encStr)
        return "".join(st)
        