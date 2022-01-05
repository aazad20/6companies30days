class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        start=0
        end=0
        ans=0
        temp=1
        while end<n:
            temp*=a[end]
            while temp>=k:
                
                temp//=a[start]
                start+=1
            ans+=end-start+1
            end+=1
        return ans
