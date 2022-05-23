# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head:):
        curr = head
        prev = None
        nextNode = None
        while curr!=None:
            if curr.val==val:
                if prev==None and curr==head:
                    curr = curr.next
                    head = curr
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr 
                curr = curr.next
        return head
    
    
            
                
        