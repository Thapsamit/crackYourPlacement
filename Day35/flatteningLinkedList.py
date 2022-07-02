def merging(l1,l2):
    dummy = Node(0)
    tempHead = dummy
    while l1!=None and l2!=None:
        if l1.data<l2.data:
            dummy.bottom = l1
            dummy = dummy.bottom
            l1 = l1.bottom
        else:
            dummy.bottom = l2
            dummy = dummy.bottom 
            l2 = l2.bottom
    if l1!=None:
        dummy.bottom = l1
    else:
        dummy.bottom = l2
    return tempHead.bottom
def flatten(root):
    if root==None or root.next==None:
        return root
    root.next = flatten(root.next)
    root = merging(root,root.next)
    return root