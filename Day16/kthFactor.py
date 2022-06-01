import math
class Solution:
    def kthFactor(self, n, k):
        i = 1
        factors = []
        while i<=int(math.sqrt(n)):
            if n%i==0:
                if n/i==i:
                    factors.append(i)
                else:
                    factors.append(i)
                    factors.append(n//i)
            i+=1
        if n not in factors:
            factors.append(n)
        factors.sort()
        if k>len(factors):
            return -1
        else:
            return factors[k-1]
            
        