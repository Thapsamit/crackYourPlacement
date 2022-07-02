"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        st = []
        curr = head 
        lastNode = None
        while curr!=None or len(st)!=0:
            if curr==None:
                if len(st)!=0:
                    popped = st[-1]
                    st.pop()
                    lastNode.next = popped.next
                    if popped.next!=None:
                        popped.next.prev = lastNode
                    curr = popped.next
                    popped.next = popped.child
                    popped.child = None
            elif curr.child!=None:
                st.append(curr)
                curr.child.prev = curr
                curr = curr.child
                lastNode = curr
            else:
                lastNode = curr
                curr = curr.next
        return head
            
        
            
        