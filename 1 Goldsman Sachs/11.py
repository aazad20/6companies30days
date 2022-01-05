class Solution:
    def findTwoElement( self,arr, n):
        ans=[0]*2
        map=[0]*(n+1)
        for i in arr:
            map[i]+=1
        for i in range(1,n+1):
            if map[i]==2:
               ans[0]=i
            if map[i]==0:
                ans[1]=i
        return ans
