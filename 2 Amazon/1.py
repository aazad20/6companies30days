class Solution:
    
    def maxProfit(self,K, N, A):
        dp= [[0 for i in range(N)] for j in range(K+1)]
        #print(dp)
        for i in range(1,K+1):
            max = -999999999999999
            for j in range(1,N):
                #print(i,j)
                if dp[i-1][j-1]-A[j-1] > max:
                    max = dp[i-1][j-1]-A[j-1]
                if max+A[j]>dp[i][j-1]:
                    dp[i][j]=max+A[j]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[K][N-1]
