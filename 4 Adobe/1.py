class Solution:
    def subArraySum(self,arr, n, s):
        start=0
        end=0
        temp=0
        while start <= end and end < n:
            temp += arr[end]
            if temp==s:
                return [start+1,end+1]
            if temp> s:
                while temp > s:
                    temp -= arr[start]
                    start+=1
                    if temp==s:
                        return [start+1,end+1]
            end+=1
        return [-1]
