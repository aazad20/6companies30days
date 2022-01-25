from collections import defaultdict
class Solution:
    def distance(self,a,b):
        return (a[0]-b[0])**2+(a[1]-b[1])**2
    
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)):
            m = defaultdict(int)
            for j in range(len(points)):
                if i==j:
                    continue
                else:
                    d = self.distance(points[i],points[j])
                    m[d]+=1
            for k in m:
                ans+=(m[k])*(m[k]-1)
        return ans
                
