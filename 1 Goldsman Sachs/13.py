class Solution:
    def decodedString(self, s):
        st,n=[],len(s)
        for i in range(n):
            if s[i]==']':
                temp=''
                while st[-1]!='[':
                    temp=st.pop()+temp
                st.pop()
                n=''
                while len(st) and st[-1].isnumeric():
                    n=st.pop()+n
                n=int(n)
                temp=temp*n
                st.append(temp)
            else:
                st.append(s[i])
        return st[0]
