class Solution:
    def find3number(self,arr, n):
        ans = []
        left = []
        l=[0]*n
        r=[0]*n
        right =[]
        for i in range(n):
            while len(left)>0 and left[-1][0]>=arr[i]:
                left.pop()
            if len(left)==0:
                l[i]=-1
                
            else:
                l[i]=left[-1][1]
            left.append((arr[i],i))
        for i in range(n-1,-1,-1):
            while len(right)>0 and right[-1][0]<=arr[i]:
                right.pop()
            if len(right)==0:
                r[i]=-1
                
            else:
                r[i]=right[-1][1]
            right.append((arr[i],i))
        for i  in range(n):
            if l[i]!=-1 and r[i]!=-1:
                ans.append(arr[l[i]])
                ans.append(arr[i])
                ans.append(arr[r[i]])
                return ans
    
        return ans
