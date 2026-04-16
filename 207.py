# class Solution:
#     def canFinish(self, num: int, prereq: List[List[int]]) -> bool:

#         indeg,neis,q={},{},[]

#         for [a,b] in prereq:
#             indeg[a]= indeg.get(a,0) + 1
#             neis[b]=neis.get(b,[])+[a]
        
#         for k in neis.keys():
#             if indeg.get(k,0)==0: q.append(k)
        
#         while q:
#             curr=q.pop()
#             for nei in neis.get(curr,[]):
#                 indeg[nei]-=1
#                 if indeg[nei]==0: q.append(nei)

#         for _,v in indeg.items():
#             if v>0: return False

#         return True
        

class Solution:
    def canFinish(self, num: int, prereq: List[List[int]]) -> bool:

        neis,vis={},{}

        for [a,b] in prereq:
            neis[b]=neis.get(b,[])+[a]
        
        def dfs(curr,vis):
            vis[curr]=1
            for nei in neis.get(curr,[]):
                if vis.get(nei)==2: continue
                if vis.get(nei)==1 or dfs(nei,vis): return True
            vis[curr]=2
            return False

        
        for k in neis.keys():
            if k not in vis and dfs(k,vis):return False

        return True
        