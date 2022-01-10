from collections import deque
class Solution:
    def FirstNonRepeating(self, A):
        q = deque()
        A=list(A)
        arr=[0]*26
        
        for i in range(len(A)):
            arr[ord(A[i])-97]+=1
            
            if arr[ord(A[i])-97]==1:
                q.append(A[i])
                    
            while len(q)>0 and arr[ord(q[0])-97]!=1:
                q.popleft()
            #print(len(q))
            if len(q)==0:
                A[i]='#'
            else:
                A[i]=q[0]
            #print(A)
       
        return "".join(A)
