
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, n):
        ans=[]
        ans.append(A[-1])
        m = A[n-1]
        for i in range(n-2,-1,-1):
            if A[i] >= m:
                ans.append(A[i])
                m = A[i]
                
        i=0
        j=len(ans)-1
        while i<j:
            ans[i],ans[j]=ans[j],ans[i]
            i+=1
            j-=1
        return ans
