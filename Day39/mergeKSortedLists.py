
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def split(self,lists):
        if len(lists)==1 or len(lists)==0:
            return lists
        l1 = lists[-1]
        l2 = lists[-2]
        lists.pop()
        lists.pop()
        newTemp = self.merging(l1,l2)
        lists.append(newTemp)
        self.split(lists)

    def merging(self,l1,l2):
        dummy = ListNode()
        temp = dummy 
        while l1 and l2:
            if l1.val<l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next
                
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        self.split(lists)
        return lists[0]
        
        