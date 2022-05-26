class Solution:
    def reverse(self, x):
        if x==0:
            return 0
        elif x<0:
            num = abs(x)
        else:
            num = x
        reverse = 0
        while num!=0:
            temp = num%10
            reverse = reverse*10 + temp
            num = num//10
        if reverse>2**31-1:
            return 0
        if x<0:
            return -reverse
        return reverse