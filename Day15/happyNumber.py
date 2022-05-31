class Solution:
    def isHappy(self, n):
        num = n
        st = set()
        while True:
            if num in st:
                return False
            else:
                st.add(num)
            total = 0
            while num!=0:
                rem = num%10
                num = num//10
                total += rem**2
            if total==1:
                return True
            else:
                num = total
            
        
                
                
        