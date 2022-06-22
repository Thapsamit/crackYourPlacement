"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        curr = head
        while curr!=None:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = temp
        curr = head
        while curr!=None:
            if curr.next!=None:
                if curr.random!=None:
                    curr.next.random = curr.random.next
                else:
                    curr.next.random = None
            curr = curr.next.next
        orig = head 
        copy = head.next
        temp = copy
        while orig!=None:
            orig.next = orig.next.next
            if copy.next!=None:
                copy.next = copy.next.next
            else:
                copy.next = None
            orig = orig.next
            copy = copy.next
        return temp
        