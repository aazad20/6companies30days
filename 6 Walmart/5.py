class Solution:
    def toSumTree(self, root) :
        def recurr(root):
            if root:
                x = recurr(root.left)
                y = recurr(root.right)
                s=x+y+root.data
                root.data =  x+y
                return s
            else:
                return 0
            
            
            
        recurr(root)
