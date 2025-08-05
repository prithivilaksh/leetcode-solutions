# class Solution:
#     def maxPoints(self, grid: List[List[int]], qs: List[int]) -> List[int]:
        
#         for i,val in enumerate(qs):qs[i]=[val,i]
#         qs.sort()

#         m,n=len(grid),len(grid[0])
#         pq=[(grid[0][0],0,0)]
#         grid[0][0],count=-1,0
#         res=[-1]*len(qs)

#         for val,ind in qs:
#             while pq and pq[0][0]<val:
#                 _,i,j=heappop(pq)
#                 count+=1
#                 for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
#                     vi,vj=di+i,dj+j
#                     if 0<=vi<m and 0<=vj<n and grid[vi][vj]!=-1:
#                         heappush(pq,(grid[vi][vj],vi,vj))
#                         grid[vi][vj]=-1
#             res[ind]=count
#         return res


class Solution:
    def maxPoints(self, grid: List[List[int]], qs: List[int]) -> List[int]:
        
        for i,val in enumerate(qs):qs[i]=[val,i]
        qs.sort()

        m,n=len(grid),len(grid[0])
        pq=[(grid[0][0],0,0)]
        grid[0][0],count=-1,0
        res=[-1]*len(qs)

        for val,ind in qs:
            tmp=[]
            while tmp or (pq and pq[0][0]<val):
                if tmp: i,j=tmp.pop()
                else: _,i,j=heappop(pq)
                count+=1
                for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                    vi,vj=di+i,dj+j
                    if 0<=vi<m and 0<=vj<n and grid[vi][vj]!=-1:
                        if grid[vi][vj]<val: tmp.append((vi,vj))
                        else: heappush(pq,(grid[vi][vj],vi,vj))
                        grid[vi][vj]=-1
            res[ind]=count
        return res

