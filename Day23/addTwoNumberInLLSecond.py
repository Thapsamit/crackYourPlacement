# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwo(self,l1,l2,pv1,pv2,ans):
        addNum = 0
        if pv1==0 and pv2==0: 
            return 0
        if pv1==pv2:
            oc = self.addTwo(l1.next,l2.next,pv1-1,pv2-1,ans)
            addNum = (l1.val+l2.val+oc)
            
        elif pv1>pv2:
            oc = self.addTwo(l1.next,l2,pv1-1,pv2,ans)
            addNum = (l1.val+oc)
            
        else:
            oc = self.addTwo(l1,l2.next,pv1,pv2-1,ans)
            addNum = (l2.val+oc)
            
        newData = addNum%10
        carry = addNum//10
        ans.append(newData)
        return carry
    def calLen(self,head):
        curr = head
        count = 0
        while curr!=None:
            count+=1
            curr = curr.next
        return count
    def createList(self,ans):
        head = None
        head = ListNode(ans[0])
        last = head
        for i in ans[1:]:
            newNode = ListNode(i)
            last.next =  newNode
            last = newNode
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.calLen(l1)
        len2 = self.calLen(l2)
        ans = []
        oc = self.addTwo(l1,l2,len1,len2,ans)
        if oc>0:
            ans.append(oc)
        ans = ans[::-1]
        newHead = self.createList(ans)
        return newHead