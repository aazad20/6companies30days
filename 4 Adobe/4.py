# User function Template for Python3
class Solution:
    def isSubsetSum (self, n, arr, sum):
        dp = [[False for _ in range(sum+1)] for _ in range(n+1)]
        for i in range(sum+1):
            dp[0][i]=False
        for i in range(n+1):
            dp[i][0]=True
            
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][sum]
    
    def equalPartition(self,N, nums):
        s = sum(nums)
        if s&1:
            return False
        s=s//2
        return self.isSubsetSum(len(nums),nums,s)
