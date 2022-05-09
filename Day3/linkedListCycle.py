class Solution(object):
    def hasCycle(self, head):
        slow = head 
        fast = head
        count = 1
        while fast!=None and fast.next!=None:
            if fast==slow and count!=1:
                return True
            fast = fast.next.next
            if fast==slow:
                return True
            slow = slow.next
            count+=1
        return False
        
        