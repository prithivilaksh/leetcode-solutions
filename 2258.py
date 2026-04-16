# class Solution:
#     def maximumMinutes(self, grid: List[List[int]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         dirs=((0,1),(1,0),(-1,0),(0,-1))
#         dq=deque()
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==0: grid[i][j]=inf
#                 elif grid[i][j]==1: grid[i][j]=0;dq.append((i,j))
#                 else: grid[i][j]=-1
        
#         d=0
#         while dq:
#             for _ in range(len(dq)):
#                 i,j=dq.popleft()
#                 for di,dj in dirs:
#                     vi,vj=i+di,j+dj
#                     if 0<=vi<m and 0<=vj<n and grid[vi][vj]==inf:
#                         grid[vi][vj]=d+1
#                         dq.append((vi,vj))
#             d+=1
        
#         def check(d):
#             if grid[0][0]<=d: return False
#             dq,vis=deque([(0,0)]),set()
#             while dq:
#                 d+=1
#                 for _ in range(len(dq)):
#                     i,j=dq.popleft()
#                     for di,dj in dirs:
#                         vi,vj=i+di,j+dj
#                         if 0<=vi<m and 0<=vj<n and (vi,vj) not in vis and d<=grid[vi][vj]:
#                             if vi==m-1 and vj==n-1: return True
#                             if d>=grid[vi][vj]: continue
#                             dq.append((vi,vj))
#                             vis.add((vi,vj))
#             return False

#         l,r,res=0,m*n,-1
#         while l<=r:
#             mid=l+(r-l)//2
#             if check(mid): res,l=mid,mid+1
#             else: r=mid-1
        
#         return 10**9 if res==m*n else res

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid),len(grid[0])
        dirs=((0,1),(1,0),(-1,0),(0,-1))
        dq=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0: grid[i][j]=inf
                elif grid[i][j]==1: grid[i][j]=0;dq.append((i,j))
                else: grid[i][j]=-1
        
        d=0
        while dq:
            for _ in range(len(dq)):
                i,j=dq.popleft()
                for di,dj in dirs:
                    vi,vj=i+di,j+dj
                    if 0<=vi<m and 0<=vj<n and grid[vi][vj]==inf:
                        grid[vi][vj]=d+1
                        dq.append((vi,vj))
            d+=1
        
        h=[(-grid[m-1][n-1],m-1,n-1)]
        while h:
            t,i,j=heappop(h)
            t=-t
            if i==0 and j==0: return t if t!=inf else 10**9
            grid[i][j]=-1
            for di,dj in dirs:
                vi,vj=i+di,j+dj
                if 0<=vi<m and 0<=vj<n and grid[vi][vj]!=-1:
                    nt=min(t-1,grid[vi][vj]-1)
                    if nt<0: continue
                    heappush(h,(-nt,vi,vj))
        return -1