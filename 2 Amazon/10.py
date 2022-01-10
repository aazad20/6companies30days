class Solution:

    def matchPairs(self,nuts, bolts, n):
        # code here
        lst = ['!','#','$','%','&','*','@','^','~']
        res = []
        for el in lst:
            if el in nuts:
                res.append(el)
        for i in range(n):
            nuts[i],bolts[i] = res[i],res[i]
