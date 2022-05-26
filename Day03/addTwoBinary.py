class Solution(object):
    def addBinary(self, a, b):
        lenA = len(a)
        lenB = len(b)
        carry = 0
        ans = ''
        if lenA<lenB:
            flag = 1
        elif lenB<lenA:
            flag = 2
        else:
            flag = 3
        ptr1 = lenA-1
        ptr2 = lenB-1
        while ptr1>=0 and ptr2>=0:
            if carry == 0:
                if a[ptr1]=='0' and b[ptr2]=='0':
                    ans+='0'
                    carry = 0
                elif (a[ptr1]=='0' and b[ptr2]=='1') or (a[ptr1]=='1' and b[ptr2]=='0'):
                    ans+='1'
                    carry = 0
                else:
                    ans+='0'
                    carry = 1
            else:
                if a[ptr1]=='0' and b[ptr2]=='0':
                    ans+='1'
                    carry = 0
                elif(a[ptr1]=='0' and b[ptr2]=='1') or (a[ptr1]=='1' and b[ptr2]=='0'):
                    ans+='0'
                    carry = 1
                else:
                    ans+='1'
                    carry = 1
            ptr1-=1
            ptr2-=1
        if flag==3:
            if carry==1:
                ans+='1'
            return ans[::-1]
        elif flag==1:
            for i in range(lenB-lenA-1,-1,-1):
                if carry==0:
                    ans+=b[i]
                else:
                    if b[i]=='0':
                        ans+='1'
                        carry = 0
                    else:
                        ans+='0'
                        carry = 1
        else:
            for i in range(lenA-lenB-1,-1,-1):
                if carry==0:
                    ans+=a[i]
                else:
                    if a[i]=='0':
                        ans+='1'
                        carry = 0
                    else:
                        ans+='0'
                        carry = 1
        if carry==1:
            ans+='1'
        return ans[::-1]
                    
            
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        