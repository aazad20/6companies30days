class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        ans = ""
        for i in string:
            if i.isnumeric() or i=="-":
                ans+=i
            else:
                return -1
        return ans
