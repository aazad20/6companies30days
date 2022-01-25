class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(val,days,weights):
            d=1
            temp=0
            for i in weights:
                temp+=i
                if temp > val:
                    temp = i
                    d+=1
            if d>days:
                return False
            return True
        
        start = max(weights)
        end = sum(weights)
        ans=0
        while start<=end:
            mid = (start+end)//2
            if possible(mid,days,weights):
                #print("Returned True",mid)
                ans= mid
                end = mid-1
            
            else:
                start=mid+1
        return ans
