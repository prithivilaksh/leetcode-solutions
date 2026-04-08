# # Kruskal's - sorting/ordering(heap) + DSU
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n=len(points)
#         par=[i for i in range(n)]
#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             if a==b: return False
#             par[b]=a
#             return True
        
#         h=[]
#         for i,(a,b) in enumerate(points):
#             for j,(c,d) in enumerate(points):
#                 if i<j:
#                     d=abs(a-c)+abs(b-d)
#                     heappush(h,(d,i,j))

#         edgecnt=res=0
#         while edgecnt<n-1:
#             d,i,j=heappop(h)
#             if union(i,j): res+=d;edgecnt+=1
#         return res


# ## Prim's - heap - like djikstra
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:

#         n=len(points)
#         cost,vis=[inf]*n,set()
#         cost[0]=res=0
#         h=[(0,0)]

#         def distance(i,j):
#             (a,b),(c,d)=points[i],points[j]
#             return abs(a-c)+abs(b-d)

#         while len(vis)!=n:
#             d,i=heappop(h)
#             if i in vis: continue
#             vis.add(i)
#             res+=d
#             for j in range(n):
#                 if j in vis: continue
#                 nd=distance(i,j)
#                 if nd<cost[j]:
#                     cost[j]=nd
#                     heappush(h,(nd,j))
#         return res

# ## Prim's - heap - like djikstra
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:

#         n=len(points)
#         cost=[inf]*n
#         cost[0]=res=cnt=0
#         h=[(0,0)]

#         def distance(i,j):
#             (a,b),(c,d)=points[i],points[j]
#             return abs(a-c)+abs(b-d)

#         while True:
#             d,i=heappop(h)
#             if cost[i]<0: continue
#             cost[i]=-1
#             res+=d
#             cnt+=1
#             if cnt==n: break
#             for j in range(n):
#                 if cost[j]<0: continue
#                 nd=distance(i,j)
#                 if nd<cost[j]:
#                     cost[j]=nd
#                     heappush(h,(nd,j))
#         return res


## Prim's - heap - like djikstra
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n=len(points)
        cost=[inf]*n
        res=i=0

        def distance(i,j):
            (a,b),(c,d)=points[i],points[j]
            return abs(a-c)+abs(b-d)

        for _ in range(n-1):
            cost[i]=-1
            minj=i
            for j in range(n): # since this is complete graph n*n no need for heap
                if cost[j]==-1: continue
                cost[j]=min(cost[j],distance(i,j))
                if cost[minj]==-1 or cost[minj]>cost[j]:
                    minj=j
            res+=cost[minj]
            i=minj

        return res

