class Solution(object):
    def intToRoman(self, num):
        multiplier = 0
        ans = '' 
        while num!=0:
            temp = num%10
            num = num/10
            if multiplier==0:
                multiplier = 1
                temp = temp*1
            else:
                multiplier = multiplier*10
                temp =  temp*multiplier
            if temp==1:
                ans+='I'
            elif temp==2:
                ans+='II'
            elif temp==3:
                ans+='III'
            elif temp==4:
                ans+='VI'
            elif temp==5:
                ans+='V'
            elif temp==6:
                ans+='IV'
            elif temp==7:
                ans+='IIV'
            elif temp==8:
                ans+='IIIV'
            elif temp==9:
                ans+='XI'
            elif temp==10:
                ans+='X'
            elif temp==20:
                ans+='XX'
            elif temp==30:
                ans+='XXX'
            elif temp==40:
                ans+='LX'
            elif temp==50:
                ans+='L'
            elif temp==60:
                ans+='XL'
            elif temp==70:
                ans+='XXL'
            elif temp==80:
                ans+='XXXL'
            elif temp==90:
                ans+='CX'
            elif temp==100:
                ans+='C'
            elif temp==200:
                ans+='CC'
            elif temp==300:
                ans+='CCC'
            elif temp==400:
                ans+='DC'
            elif temp==500:
                ans+='D'
            elif temp==600:
                ans+='CD'
            elif temp==700:
                ans+='CCD'
            elif temp==800:
                ans+='CCCD'
            elif temp==900:
                ans+='MC'
            elif temp==1000:
                ans+='M'
            elif temp==2000:
                ans+='MM'
            elif temp==3000:
                ans+='MMM'
    
                
        return ans[::-1]        
            
        
    