def findLen(node):
    curr = node
    count = 0
    while curr:
        count+=1
        curr = curr.next
    return count
def addZeroes(small,diff):
    dummy = Node(0)
    diff-=1
    temp = dummy
    while diff>0:
        diff-=1
        curr  = Node(0)
        temp.next = curr
        temp = curr
    temp.next = small 
    
    return dummy

def removeZeroes(node):
    curr = node
    
    while curr and curr.data==0:
        curr = curr.next
        

    return curr
        
def subtractHelper(l1,l2,borrow):
    if l1==None and l2==None and not borrow[0]:
        return None
    
    if l1!=None:
        nextL1 = l1.next
    if l2!=None:
        nextL2 = l2.next
    prev = subtractHelper(nextL1,nextL2,borrow)
    d1 = l1.data
    d2 = l2.data
    sub = 0
   
    if(borrow[0]):
        d1 = d1-1
        borrow[0] = False
    if d1<d2:
        borrow[0]=True
        d1 = d1+10
     
    sub = d1-d2
    curr = Node(sub)
    curr.next = prev 
    return curr
        

    
def subLinkedList(l1, l2):
    if l1==None and l2==None:
        return None
    l1 = removeZeroes(l1)
    l2 = removeZeroes(l2)
    lenL1 = findLen(l1)
    lenL2 = findLen(l2)
    large = l1
    small = l2
    if lenL1!=lenL2:
        if lenL1>lenL2:
            large = l1 
            small = l2
        else:
            large = l2
            small = l1
        small = addZeroes(small,abs(lenL1-lenL2))
    else:
        curr1 = l1 
        curr2 = l2
        while curr1!=None and curr2!=None:
            if curr1.data!=curr2.data:
                if curr1.data>curr2.data:
                    large = l1 
                    small = l2
                else:
                    large = l2 
                    small = l1
                break
            curr1 = curr1.next 
            curr2 = curr2.next
    borrow = [False]    
    subtraction = subtractHelper(large,small,borrow)
    subtraction = removeZeroes(subtraction)
    if subtraction==None:
        return Node(0)
    return subtraction