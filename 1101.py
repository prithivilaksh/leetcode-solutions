from typing import List
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        par,cnt=list(range(n)),1

        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        def union(a,b):
            a,b=find(a),find(b)
            par[a]=b
            return a!=b
        for ts,a,b in logs:
            if union(a,b): cnt+=1
            if cnt==n: return ts

        return -1
            
print(Solution().earliestAcq(logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6))
print(Solution().earliestAcq(logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4))
