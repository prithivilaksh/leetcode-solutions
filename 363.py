# # TLE
# class Solution:
#     def maxSumSubmatrix(self, mat: List[List[int]], k: int) -> int:

#         m,n,res=len(mat),len(mat[0]),-10**6

#         for i in range(m):
#             for j in range(n):
#                 if i-1>=0: mat[i][j]+=mat[i-1][j]
#                 if j-1>=0: mat[i][j]+=mat[i][j-1]
#                 if i-1>=0 and j-1>=0: mat[i][j]-=mat[i-1][j-1]
        
#         for i1 in range(m):
#             for j1 in range(n):
#                 for i2 in range(i1,m):
#                     for j2 in range(j1,n):
#                         area=mat[i2][j2]
#                         if i1-1>=0: area-=mat[i1-1][j2]
#                         if j1-1>=0: area-=mat[i2][j1-1]
#                         if i1-1>=0 and j1-1>=0: area+=mat[i1-1][j1-1]
#                         if area<=k: 
#                             res=max(res,area)
#                             if area==k: return k
#         return res


# class Solution:
#     def maxSumSubmatrix(self, mat: List[List[int]], k: int) -> int:

#         m,n,res=len(mat),len(mat[0]),-inf

#         for l in range(n):
#             rowsum=[0]*m
#             for r in range(l,n):
#                 for i in range(m):
#                     rowsum[i]+=mat[i][r]
                
#                 sums,csum,mx=[0],0,-inf
#                 for s in rowsum:
#                     csum+=s
#                     pos=bisect_left(sums,csum-k)
#                     if pos!=len(sums): mx=max(mx,csum-sums[pos])
#                     insort(sums,csum)
#                 res=max(res,mx)
#                 if res==k: return k
#         return res

class Solution:
    def maxSumSubmatrix(self, mat: List[List[int]], k: int) -> int:

        m,n,res=len(mat),len(mat[0]),-inf

        for l in range(n):
            rowsum=[0]*m
            for r in range(l,n):
                for i in range(m):
                    rowsum[i]+=mat[i][r]
                
                csum,mx=0,-inf
                for s in rowsum:
                    csum=max(csum+s,s)
                    mx=max(mx,csum)

                if mx>k:
                    sums,csum,mx=[0],0,-inf
                    for s in rowsum:
                        csum+=s
                        pos=bisect_left(sums,csum-k)
                        if pos!=len(sums): mx=max(mx,csum-sums[pos])
                        insort(sums,csum)
                res=max(res,mx)
                if res==k: return k
        return res