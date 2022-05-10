class Solution(object):
    def validPalindrome(self, s):
        start = 0 
        end = len(s)-1
        while start<end:
            if s[start]!=s[end]:
                left = s[start:end]
                right = s[start+1:end+1]
                if left==left[::-1]:
                    return True
                elif right==right[::-1]:
                    return True
                else:
                    return False
            start+=1
            end-=1
        return True
        
        
                    
       
        """
        :type s: str
        :rtype: bool
        """
        