class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0 
        end = 0
        ans= 999999
        temp=0
        n = len(nums)
        while end<n:
            temp+=nums[end]
            if temp<target:
                end+=1
            elif temp >= target:
                while temp>=target:
                    ans = min(ans,(end-start+1))
                    temp-=nums[start]
                    start+=1
                end+=1
                
        if ans==999999 or ans<0:
            return 0
        else:
            return ans
