def middleNode(self, head):
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
    return slow