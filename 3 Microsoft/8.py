from collections import deque
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        q = deque()
        q.append(root)
        while(len(q)>0):
            size = len(q)
            for i in range(size):
                temp = q[0]
                q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                if i+1==size:
                    temp.nextRight=None
                else:
                    temp.nextRight=q[0]
