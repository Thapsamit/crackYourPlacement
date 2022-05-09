class Solution(object):
    def deleteDuplicates(self, head):
        ptr = head
        tempNode = head
        while ptr!=None:
            if tempNode.val!=ptr.val:
                tempNode.next = ptr
                tempNode = ptr
            ptr = ptr.next
        if tempNode!=None:
            tempNode.next = None
        return head