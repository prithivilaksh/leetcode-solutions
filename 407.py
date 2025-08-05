# class Solution:
#     def trapRainWater(self, height: List[List[int]]) -> int:
        
#         m,n=len(height),len(height[0])
#         if m<=2 or n<=2: return 0
#         q=[]
#         for i in range(m):
#             for j in (0,n-1):
#                 if height[i][j]!=-1:
#                     heappush(q,(height[i][j],i,j))
#                     height[i][j]=-1     
#         for j in range(n):
#             for i in (0,m-1):
#                 if height[i][j]!=-1:
#                     heappush(q,(height[i][j],i,j))
#                     height[i][j]=-1  

#         res=mxh=0

#         while q:
#             h,i,j=heappop(q)
#             mxh=max(mxh,h)
#             # res+=mxh-h
#             for di,dj in((0,1),(1,0),(-1,0),(0,-1)):
#                 vi,vj=di+i,dj+j
#                 if 0<=vi<m and 0<=vj<n and height[vi][vj]!=-1:
#                     heappush(q,(height[vi][vj],vi,vj))
#                     res+=(max(0,mxh-height[vi][vj]))
#                     height[vi][vj]=-1
#         return res


class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        
        m,n=len(height),len(height[0])
        if m<=2 or n<=2: return 0
        q=[]
        for i in range(m):
            for j in (0,n-1):
                if height[i][j]!=-1:
                    heappush(q,(height[i][j],i,j))
                    height[i][j]=-1     
        for j in range(n):
            for i in (0,m-1):
                if height[i][j]!=-1:
                    heappush(q,(height[i][j],i,j))
                    height[i][j]=-1  

        res=mxh=0

        while q:
            h,i,j=heappop(q)
            mxh=max(mxh,h)
            res+=mxh-h
            for di,dj in((0,1),(1,0),(-1,0),(0,-1)):
                vi,vj=di+i,dj+j
                if 0<=vi<m and 0<=vj<n and height[vi][vj]!=-1:
                    heappush(q,(height[vi][vj],vi,vj))
                    height[vi][vj]=-1
        return res
            