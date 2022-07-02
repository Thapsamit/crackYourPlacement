class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None:
            return None
        sLeft = None
        leftHead = None
        lLeft = None
        rightHead = None
        curr = head 
        while curr!=None:
            if curr.val<x:
                if leftHead == None:
                    leftHead = curr
                if sLeft==None or sLeft.next==curr:
                    sLeft = curr
                else:
                    sLeft.next = curr 
                    sLeft = curr
            else:
                if rightHead==None:
                    rightHead = curr
                if lLeft==None or lLeft.next==curr:
                    lLeft = curr
                else:
                    lLeft.next = curr
                    lLeft = curr
            curr = curr.next
        if rightHead!=None and leftHead!=None:
            sLeft.next = rightHead
            lLeft.next = None
            return leftHead
        if rightHead==None:
            return leftHead
        if leftHead==None:
            return rightHead
            