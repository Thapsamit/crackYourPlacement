class Solution:
    def merge(self,leftHead,rightHead):
        
        newHead = Node(None)
        temp = newHead
        
        while leftHead!=None and rightHead!=None:
            if leftHead.data<rightHead.data:
                temp.next = leftHead
                leftHead = leftHead.next
                temp = temp.next
            else:
                temp.next = rightHead
                rightHead = rightHead.next
                temp = temp.next
        if leftHead!=None:
            temp.next = leftHead
        if rightHead!=None:
            temp.next = rightHead
        return newHead.next
    def findMid(self,head):

        fast = head
        slow = head
        prev = None
        while fast!=None and fast.next!=None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow
        
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        
        if head==None or head.next==None:
            return head
        mid = self.findMid(head)
    
        leftPart = self.mergeSort(head)
        rightPart = self.mergeSort(mid)
        
        
        combine = self.merge(leftPart,rightPart)
        return combine