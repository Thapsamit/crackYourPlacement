class Solution:
    def reverseBetween(self, head, left, right):
        node = head
        count = 1
        prevNode = None
        while node!=None:
            if count==left:
                curr = node
                prev = None
                nextNode = None
                totalNodes = right-left+1
                c = 0
                while c!=totalNodes:
                    nextNode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextNode
                    c+=1
                node.next = curr
                if prevNode!=None:
                    prevNode.next = prev
                if left==1:
                    return prev
                else:
                    return head
            else:
                count+=1
                prevNode = node
                node = node.next