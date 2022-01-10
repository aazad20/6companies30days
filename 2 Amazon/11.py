    
    if not root:
        A.append(-1)
        return None
        
    #storing the data at node in list.
    A.append(root.data)
    
    #calling function recursively for left and right subtrees.
    serialize(root.left, A)
    serialize(root.right, A)


#Function to construct the tree.    
def func(A):
    
    #base case if there are no more elements in list.
    if(func.index==len(A) or A[func.index]==-1):
        func.index=func.index+1
        return None
    
    #creating new node for storing current element.    
    node = Node(A[func.index])
    func.index=func.index+1
    
    #calling function recursively for left and right subtrees.
    node.left = func(A)
    node.right = func(A)
    return node

#Function to deserialize a list and construct the tree.    
def deSerialize(A):
    func.index=0
    #returning the tree.
    return func(A)
    
