from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(0, len(edges)):
            graph[edges[i][0]].append((succProb[i], edges[i][1]))
            graph[edges[i][1]].append((succProb[i], edges[i][0]))     
        visited = set()
        heap = [(-1, start)]
        while heap:
            prob, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return -prob
            
            for n_prob, n_node in graph[node]:
                running_prob = prob * n_prob
                heapq.heappush(heap, (running_prob, n_node))
                
        return 0
