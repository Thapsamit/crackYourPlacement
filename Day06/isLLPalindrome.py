class Solution:
    def isPalindrome(self, head):
        firstHalf = []
        secondHalf = []
        fast = head
        slow = head
        firstHalf.append(slow.val)
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            firstHalf.append(slow.val)
        while slow!=None:
            secondHalf.append(slow.val)
            slow = slow.next
        if (len(firstHalf)+len(secondHalf))%2!=0:
            firstHalf.pop()
        secondHalf.reverse()
        return firstHalf==secondHalf