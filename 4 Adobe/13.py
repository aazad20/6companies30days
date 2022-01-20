#User function Template for python3
import bisect

class Solution:
    
    # Function to get length of the Longest Increasing Subsequence
    # in NlogN time.
    def LISLength(self, v):
        if len(v) == 0:  # boundary case
            return 0
     
        tail = [0 for i in range(len(v) + 1)]
        length = 1  # always points empty slot in tail
     
        tail[0] = v[0]
     
        for i in range(1, len(v)):
            if v[i] > tail[length-1]:
                # v[i] extends the largest subsequence
                tail[length] = v[i]
                length += 1
            else:
                tail[bisect.bisect_left(tail, v[i], 0, length-1)] = v[i]
     
        return length
        
    def minInsAndDel(self, A, B, N, M):
        mp = dict()
        for i in range(M):
            mp[B[i]] = i 
        
        res = []
        
        for i in range(N):
            if A[i] in mp:
                res.append(mp[A[i]])
        
        ans = (N-self.LISLength(res)) + (M-self.LISLength(res))
        
        return ans
