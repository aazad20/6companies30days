from collections import deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        q = deque()
        i=0
        ans=[]
        while i<n:
            if len(q)>0 and q[0]==i-k:
                q.popleft()
            while len(q)>0 and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
            if i>= k-1:
                ans.append(arr[q[0]])                                                        
            i+=1
        return ans
