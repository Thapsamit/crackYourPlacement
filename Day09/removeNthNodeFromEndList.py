# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLength(self,head):
        curr = head
        count = 0
        while curr!=None:
            count+=1
            curr = curr.next
        return count
    def removeNthFromEnd(self, head, n):
        findLen = self.findLength(head)
        if n>findLen:
            return head
        leftElements = findLen-n
        curr = head
        c = 1
        while c<leftElements:
            curr = curr.next
            c+=1
        if leftElements==0:
            head = curr.next
        else:
            curr.next = curr.next.next
        return head