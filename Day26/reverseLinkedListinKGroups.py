# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversingK(self,node,i,tt,k):
        if i==tt or node==None:
            return node
        start = node
        prev = None
        curr = node
        nextNode = None
        c = 0
        while curr!=None and c<k:
            nextNode = curr.next 
            curr.next = prev
            prev = curr 
            curr = nextNode
            c+=1
        start.next = self.reversingK(nextNode,i+1,tt,k)
        return prev
    
    def findLen(self,head):
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLen = self.findLen(head)
        tt = listLen//k
        head = self.reversingK(head,0,tt,k)
        return head
            
        