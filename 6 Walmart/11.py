import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        r=[]
        ans=0
        for x in range(len(speed)):
            r.append([efficiency[x],speed[x]])
            ans=max(ans,efficiency[x]*speed[x])
        if k==1:
            return ans
        r.sort()
        sum=[0 for x in range(len(speed))]
        p=[]
        i=len(speed)-1
        sum[i]=r[-1][1]
        p.append(sum[i])
        i=i-1
        for x in range(k-2):
            sum[i]=sum[i+1]+r[i][1]
            p.append(r[i][1])
            i=i-1
        heapq.heapify(p)
        for x in range(len(speed)-(k-1)-1,-1,-1):
            y=heapq.heappop(p)
            if r[x][1]>y:
                sum[x]=sum[x+1]-y+r[x][1]
            else:
                sum[x]=sum[x+1]
            y=max(y,r[x][1])
            heapq.heappush(p,y)
        for x in range(len(r)):
            if x==len(r)-1:
                ans=max(ans,r[x][0]*sum[x])   
            else:
                ans=max(ans,r[x][0]*(sum[x+1]+r[x][1]))
        return ans%1000000007
