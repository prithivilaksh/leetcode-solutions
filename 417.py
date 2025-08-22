# class Solution:
#     def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:

#         m,n=len(h),len(h[0])
#         vis1=[[False]*n for i in range(m)]
#         vis2=[[False]*n for i in range(m)]

#         q=deque([(0,0)])
#         for i in range(1,m):q.append((i,0))
#         for j in range(1,n):q.append((0,j))

#         while q:
#             i,j=q.popleft()
#             vis1[i][j]=True
#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 ni,nj=i+di,j+dj
#                 if 0<=ni<m and 0<=nj<n and not vis1[ni][nj] and h[i][j]<=h[ni][nj]:
#                     q.append((ni,nj))
        
#         q=deque([(m-1,n-1)])
#         for i in range(m-1):q.append((i,n-1))
#         for j in range(n-1):q.append((m-1,j))

#         while q:
#             i,j=q.popleft()
#             vis2[i][j]=True
#             for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                 ni,nj=i+di,j+dj
#                 if 0<=ni<m and 0<=nj<n and not vis2[ni][nj] and h[i][j]<=h[ni][nj]:
#                     q.append((ni,nj))
            
#         res=[]
#         for i in range(m):
#             for j in range(n):
#                 if vis1[i][j] and vis2[i][j]: res.append([i,j])
        
#         return res

class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:

        m,n=len(h),len(h[0])
        dirs=((0,1),(1,0),(-1,0),(0,-1))
        def bfs(q):
            vis=set()
            while q:
                i,j=q.pop()
                vis.add((i,j))
                for di,dj in dirs:
                    ni,nj=i+di,j+dj
                    if 0<=ni<m and 0<=nj<n and (ni,nj) not in vis and h[i][j]<=h[ni][nj]:
                        q.append((ni,nj))
            return vis

        q=[(0,0)]
        for i in range(1,m):q.append((i,0))
        for j in range(1,n):q.append((0,j))
        vis1=bfs(q)
        q=[(m-1,n-1)]
        for i in range(m-1):q.append((i,n-1))
        for j in range(n-1):q.append((m-1,j))
        vis2=bfs(q)
        
        return list(vis1&vis2)
