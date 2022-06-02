def multiplyTwoList(head1, head2):
    n1 = 0
    n2 = 0
    mod = 1000000007
    while head1!=None or head2!=None:
        if head1!=None:
            n1 = ((n1*10)+head1.data)%mod
            head1 = head1.next
        if head2!=None:
            n2 = ((n2*10)+head2.data)%mod
            head2 = head2.next
    return (n1%mod * n2%mod)%mod