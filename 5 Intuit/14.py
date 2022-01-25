class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q= deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append([(i,j),0])
        if not q :
            return -1
        ans =0
        while q:
            (i,j),c=q.popleft()
            ans = max(ans,c)
            for k,l in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj=k+i,l+j
                if 0<=ni<len(grid) and 0<= nj < len(grid[0]) and grid[ni][nj]==0:
                    grid[ni][nj]=c+1
                    q.append([(ni,nj),c+1])
        return ans if ans else -1
