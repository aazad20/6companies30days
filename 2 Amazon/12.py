class Solution:
    def colName (self, n):
        temp =""
        while n>0:
            ch = chr(65+(n-1)%26)
            temp=ch+temp
            n=(n-1)//26
        return temp
