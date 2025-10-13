class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2: return 0

        @cache
        def dist(i,j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])

        def check(k):
            color = [-1]*n
            for start in range(n):
                if color[start] != -1: continue
                color[start] = random.randint(0,100) ## can be any random integer for 1 search
                q = deque([start])
                while q:
                    u = q.popleft()
                    for v in range(n):
                        if u == v: continue
                        if dist(u,v) < k:
                            if color[v] == -1:
                                color[v] = color[u]^1
                                q.append(v)
                            elif color[v] == color[u]:
                                return False
            return True
                
        res=0        
        l,r=0,10**9
        while l<=r:
            m=l+(r-l)//2
            if check(m): res,l=m,m+1
            else: r=m-1
        return res