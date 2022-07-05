class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        curr = ""
        for i in path+'/':
            if i=='/':
                if curr=="..":
                    if st:
                        st.pop()
                elif curr!="" and curr!=".":
                    st.append(curr)
                curr=""
            else:
                curr+=i
        return "/"+"/".join(st)
        