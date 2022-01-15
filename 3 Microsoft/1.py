class Solution:
	def minDifference(self, arr, n):
	    s = sum(arr)
	    temp=1 if s&1 else 0
	    s=s//2
	    dp = [ [0 for _ in range(s+1)] for _ in range(n+1)]
	    for i in range(1,n+1):
	        for j in range(1,s+1):
	            if arr[i-1]<=j:
	                dp[i][j] = max(arr[i-1]+dp[i-1][j-arr[i-1]],dp[i-1][j])
	            else:
	                dp[i][j]=dp[i-1][j]
	    ans =dp[n][s]
	    return (2*s+temp-ans)-ans
