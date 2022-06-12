def reverseList(head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head
def findMid(head):
    fast = head
    slow = head
    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
    return slow
def reorderList(self):
    mid = findMid(self.head)
    revStartPoint = reverseList(mid.next)
    mid.next = None
    curr1 = self.head
    curr2 = revStartPoint
    alternate = 1
    while curr1!=None and curr2!=None:
        if alternate%2!=0:
            temp = curr1.next
            curr1.next = curr2
            curr1 = temp
        else:
            temp = curr2.next
            curr2.next = curr1
            curr2 = temp
        alternate+=1
        
    return self.head