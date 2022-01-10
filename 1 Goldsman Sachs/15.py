class Solution:
	def canPair(self, nums, k):
	    if len(nums)%2!=0:
	        return False
	    map = {}
	    for i in nums:
	        temp = i%k
	        if temp in map:
	            map[temp]+=1
	        else:
	            map[temp]=1
	    for i in nums:
	        temp = i%k
	        if temp==0:
	            if map[0]&1:
	                return False
	        elif k-temp not in map or map[temp]!=map[k-temp]:
	            return False
	    return True
