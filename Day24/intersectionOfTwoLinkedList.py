# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findLength(self,node):
        curr = node
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        size1 = self.findLength(headA)
        size2 = self.findLength(headB)
        diff = abs(size1-size2)
        curr1 = headA
        curr2 = headB
        if size1>size2:
            for i in range(0,diff,1):
                curr1 = curr1.next
        else:
            for i in range(0,diff,1):
                curr2 = curr2.next
        while curr1!=curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1
        