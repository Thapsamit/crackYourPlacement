class Solution(object):
    def getTotal(self,head):
        ptr = head
        count = 0
        while ptr!=None:
            count+=1
            ptr = ptr.next
        return count
    def getDecimalValue(self, head):
        totalNodes = self.getTotal(head)
        ptr = head
        total = 0
        totalNodes = totalNodes-1
        while ptr!=None:
            total+=ptr.val*(2**totalNodes)
            ptr = ptr.next
            totalNodes-=1
        return total