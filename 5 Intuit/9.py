class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        p =[(i,0) for i in range(len(heights))] + [(0,i) for i in range(len(heights[0]))]
        
        a = [(len(heights)-1,i) for i in range(len(heights[0]))]+[(i,len(heights[0])-1)  for i in range(len(heights))]
        
        
        
        
        
        def bfs(p,prev,res):
            row,col = p
            row_p,col_p = prev
            if p not in res and 0<=row < len(heights) and 0<=col<len(heights[0]) and heights[row][col] >=heights[row_p][col_p]:
                res.add(p)
                bfs((row+1,col),p,res)
                bfs((row,col+1),p,res)
                bfs((row-1,col),p,res)
                bfs((row,col-1),p,res)
                
        for i in p:
            bfs(i,i,pacific)
        
        for i in a:
            bfs(i,i,atlantic)
        return pacific.intersection(atlantic)
        
