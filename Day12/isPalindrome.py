class Solution:
    def isPalindrome(self, x):
        if x==0:
            return True
        if x<0:
            return False
        temp = x
        res = 0
        while temp!=0:
            rem = temp%10
            res = res*10+rem
            temp = temp//10
        return res==x
        