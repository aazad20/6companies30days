#User function Template for python3

class Solution:
    #Complete this function
    
    def power(self,N,R,mod = 1000000007):
        res = 1
        while R>0:
            if R%2==0:
                N = (N%mod * N%mod)%mod
                R//=2
            else:
                res=(res%mod*N%mod)%mod
                R-=1
        return res%mod
                
        #Your code here
