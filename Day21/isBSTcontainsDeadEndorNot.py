def storeNodes(root,allNodes,leafs):
    if root==None:
        return 
    allNodes.add(root.data)
    if root.left==None and root.right==None:
        leafs.add(root.data)
        return 
    storeNodes(root.left,allNodes,leafs)
    storeNodes(root.right,allNodes,leafs)
    
    
def isdeadEnd(root):
    allNodes = set()
    leafs = set()
    allNodes.add(0)
    storeNodes(root,allNodes,leafs)
    for i in leafs:
        if i+1 in allNodes and i-1 in allNodes:
            return True
    return False