class Solution:
    def convertToTitle(self, columnNumber):
        num = columnNumber
        out = ""
        while num!=0:
            rem = num%26
            if rem==0:
                out=chr(64+26)+out
            else:
                out = chr(64+rem)+out
            
            num = (num-1)//26
        return out
        