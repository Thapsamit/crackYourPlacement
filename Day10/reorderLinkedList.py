# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversing(self,node):
        prev = None
        curr = node
        nextN=None
        while (curr != None):
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN
        node = prev
        return node
    def reorderList(self, head:):
        fast = head.next
        slow = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        curr1 = head
        curr2 = slow.next
        slow.next = None
        curr2 = self.reversing(curr2)
        while curr2:
            temp = curr1.next
            curr1.next = curr2
            curr1 = curr2
            curr2 = temp
        
        
        
        
        """
        Do not return anything, modify head in-place instead.
        """
        