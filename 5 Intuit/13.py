class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:	
        N = len(grid)
        def count_zeros(row):
            i = len(row) - 1
            while i >= 0 and not row[i]:
                i -= 1
            return len(row) - 1 - i
        zeros = [count_zeros(row) for row in grid]
        def find_nearest_alter(i, demand):
            cost = 0
            j = i
            while j < N and (zeros[j] < demand):
                
                cost += (zeros[j] >= 0)
                j += 1
            return j, cost

        i = res = shift = 0
        while i + shift < N:
           
            if zeros[i] < 0:
                i += 1
                shift -= 1
                continue
            demand = N - (i + shift) - 1
            if zeros[i] < demand:
                j, cost = find_nearest_alter(i, demand)
                if j == N:
                    return -1
                zeros[j] = -1
                res += cost
                shift += 1
            else:
                i += 1
        return res
