# class Solution:
#     def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
#         n,m=len(moveTime),len(moveTime[0])
#         d=defaultdict(lambda:inf)
#         h=[(0,0,0,1)]
#         d[0,0,1]=0

#         while h:
#             t,i,j,off=heappop(h)
#             if t>d[(i,j,off)]: continue
#             if i==n-1 and j==m-1: return t
            
#             nextoff=2 if off==1 else 1
#             for di,dj in (-1,0),(1,0),(0,-1),(0,1):
#                 x,y=i+di,j+dj
#                 if 0<=x<n and 0<=y<m:
#                     mt=max(t,moveTime[x][y])
#                     if d[x,y,nextoff]<=mt+off: continue
#                     d[x,y,nextoff]=mt+off
#                     heappush(h,(mt+off,x,y,nextoff))


            

# class Solution:
#     def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
#         n,m=len(moveTime),len(moveTime[0])
#         d=defaultdict(lambda:inf)
#         h=[(0,0,0,1)]
#         d[0,0]=0

#         while h:
#             t,i,j,off=heappop(h)
#             if t>d[i,j]: continue
#             if i==n-1 and j==m-1: return t
            
#             nextoff=2 if off==1 else 1
#             for di,dj in (-1,0),(1,0),(0,-1),(0,1):
#                 x,y=i+di,j+dj
#                 if 0<=x<n and 0<=y<m:
#                     mt=max(t,moveTime[x][y])
#                     if d[x,y]<=mt+off: continue
#                     d[x,y]=mt+off
#                     heappush(h,(mt+off,x,y,nextoff))


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        # idea/obs
        # 1) why we are not tracking distance? vis set is enough because, the time offset will be same for every cell irrespective of the path. And the fast relaxation is always the best

        n,m=len(moveTime),len(moveTime[0])
        vis=set((0,0))
        h=[(0,0,0,1)]

        while True:
            t,i,j,off=heappop(h)            
            nextoff=2 if off==1 else 1

            for di,dj in (-1,0),(1,0),(0,-1),(0,1):
                x,y=i+di,j+dj
                if 0<=x<n and 0<=y<m and (x,y) not in vis:
                    mt=max(t,moveTime[x][y])+off
                    if x==n-1 and y==m-1: return mt
                    vis.add((x,y))
                    heappush(h,(mt,x,y,nextoff))

