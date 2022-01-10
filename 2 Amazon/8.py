def countWays(self,n):
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
            
        i=3
        while i<=n:
            if i %2==0:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i-1]
            i+=1
        #print(dp)
        return dp[n]
