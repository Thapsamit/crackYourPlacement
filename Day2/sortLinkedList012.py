def segregate(self, head):
    ptr = head
    countZero = 0
    countOne = 0
    countTwo = 0
    while ptr is not None:
        if ptr.data==0:
            countZero+=1
        elif ptr.data==1:
            countOne+=1
        else:
            countTwo+=1
        ptr = ptr.next
    temp = head
    while temp is not None:
        if countZero!=0:
            temp.data = 0
            countZero-=1
        elif countOne!=0:
            temp.data = 1
            countOne-=1
        else:
            temp.data = 2
            countTwo-=1
                
        temp = temp.next 
            
    return head