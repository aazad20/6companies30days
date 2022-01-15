class Solution:
    def isPossible(self,N,p):
        adj=[[] for _ in range(N)]
        #print(adj)
        indegree=[0]*N
        for i in p:
            adj[i[0]].append(i[1])
        #print(adj)
        
        for i in range(N):
            for j in adj[i]:
                indegree[j]+=1
        #print(indegree)
        q=[]
        for i in range(N):
            if indegree[i]==0:
                q.append(i)
        
                
        ans=0
        while len(q)>0:
            node = q[0]
            ans+=1
            #print(q)
            q.pop(0)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        #print(ans)
        if N == ans:
            return True
        else:
            return False
