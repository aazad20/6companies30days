#User function Template for python3
class Solution:
	def numOfWays(self, n, x):
	    dp=[0]*(n+1)
	    dp[0]=1
	    mod = 1000000007
	    for i in range(1,n+1):
	        for j in range(n,i-1,-1):
	            y = pow(i,x)
	            if j>=y:
	                dp[j]=(dp[j]+dp[j-y])%mod
	    return dp[n]
