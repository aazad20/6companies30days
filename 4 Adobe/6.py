#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        s = []
        v=[]
        def generate(s,l,r):
            if l==0 and r==0:
                v.append("".join(s))
                return
            if l>0:
                s.append('(')
                generate(s,l-1,r)
                s.pop()
            if r>0:
                if l<r:
                    s.append(')')
                    generate(s,l,r-1)
                    s.pop()
        
        
        generate(s,n,n)
        return v
