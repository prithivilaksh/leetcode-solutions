class Solution:
    def maximumScore(self, score: list[int], edges: list[list[int]]) -> int:
        
        # idea:
        # 1) for every node maintain top 3 adjacent nodes

        top3=defaultdict(list)
        for u,v in edges:
            su,sv=score[u],score[v]
            heappush(top3[u],(sv,v))
            heappush(top3[v],(su,u))
            if len(top3[u])>3: heappop(top3[u])
            if len(top3[v])>3: heappop(top3[v])
        
        res=-1
        for u,v in edges:
            su,sv=score[u],score[v]
            for sy,y in top3[u]:
                if y==v: continue
                for sz,z in top3[v]:
                    if z==u or y==z: continue
                    res=max(res,su+sv+sy+sz)
        return res

