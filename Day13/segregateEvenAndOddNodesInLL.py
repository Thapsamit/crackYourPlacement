class Solution:
    def divide(self, N, head):
        firstOdd = None
        lastOdd = None
        firstEven = None
        lastEven = None
        curr = head
        while curr!=None:
            if curr.data % 2!=0:
                if firstOdd==None:
                    firstOdd = curr
                    lastOdd = curr
                else:
                    lastOdd.next = curr
                    lastOdd = curr
            else:
                if firstEven==None:
                    firstEven = curr
                    lastEven = curr
                else:
                    lastEven.next = curr
                    lastEven = curr
            curr = curr.next
        if firstEven==None:
            return firstOdd
        if firstOdd == None:
            return firstEven
        lastEven.next = firstOdd
        lastOdd.next = None
        return firstEven