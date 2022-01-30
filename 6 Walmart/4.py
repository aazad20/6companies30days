class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        dp = [[0 for _ in range(b)] for _ in range(a)]
        for i in range(a):
            dp[i][-1]=1
        for j in range(b):
            dp[-1][j]=1
        
        
        for i in range(a-2,-1,-1):
            for j in range(b-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
