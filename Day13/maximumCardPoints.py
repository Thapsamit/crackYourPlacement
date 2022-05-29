class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        if n==k:
            return sum(cardPoints)
        if k==1:
            return max(cardPoints[0],cardPoints[n-1])
        bsf = sum(cardPoints[0:k])
        tsf = bsf
        for i in range(k-1,-1,-1):
            tsf += cardPoints[i+len(cardPoints)-k]-cardPoints[i]
            bsf = max(bsf,tsf)
        return bsf
            
        