class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic=defaultdict(list)
        visited =[0]*(numCourses)
        stack=[]
        for k,v in prerequisites:
            dic[v].append(k)
            visited[k]+=1
            
        def dfs(n):
            stack.append(n)
            visited[n]=-1
            
            for i in dic[n]:
                visited[i]-=1
                if visited[i]==0:
                    dfs(i)
            
                
        
        
        for i in range(numCourses):
            if visited[i]==0:
                dfs(i)
        if len(stack)==numCourses:
            return stack
        else:
            return []
