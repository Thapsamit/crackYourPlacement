from collections import defaultdict
class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, t):
        dm = defaultdict(lambda:0)
        hm = defaultdict(lambda:0)
        for i in range(0,len(t),1):
            dm[t[i]]+=1
            
        count = 0
        dmCount = sum(dm.values())
        start = -1
        end = -1
        ans=""
        mini = 999999
    
        while True:
            f1 = False
            f2 = False
            while end<len(s)-1 and count<dmCount:
                end+=1
                ch = s[end]
                hm[ch]+=1
                if ch in dm:
                    if hm[ch]<=dm[ch]:

                        count+=1
                f1 = True
        
            while start<end and count==dmCount:
                if end-(start+1)-1<mini:
                    ans = s[start+1:end+1]
                    mini = min(mini,end-(start+1)-1)
                    
                start+=1
                ch = s[start]
                if hm[ch]==1:
                    hm.pop(ch)
                else:
                    hm[ch]-=1
                if ch in dm:
                    if hm[ch]<dm[ch]:
                        count-=1
                f2 = True
            if f1==False and f2==False:
                break
        if ans=="":
            return -1
        return ans