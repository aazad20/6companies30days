def countSubtreesWithSumX(root, x):
    res=0
    def ans(root,x):
        nonlocal res
        if root==None:
            return 0
        left = ans(root.left,x)
        right = ans(root.right,x)
        s = root.data+left+right
        if s==x:
            res+=1
        return s
    ans(root,x)
    return res
