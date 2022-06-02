def findPreSuc(root, pre, suc, key):
    if root==None:
        return 

    if root.key<key:
        pre[0] = root
        findPreSuc(root.right,pre,suc,key)
    elif root.key>key:
        suc[0] = root
        findPreSuc(root.left,pre,suc,key)
    else:
        findPreSuc(root.left,pre,suc,key)
        findPreSuc(root.right,pre,suc,key)