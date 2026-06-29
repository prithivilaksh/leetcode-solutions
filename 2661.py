# class Solution:
#     def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
#         m,n=len(mat),len(mat[0])

#         pos={}
#         for i in range(m):
#             for j in range(n):
#                 pos[mat[i][j]]=(i,j)
        
#         col,row=[m]*n,[n]*m
#         for i,a in enumerate(arr):
#             x,y=pos[a]
#             row[x]-=1
#             col[y]-=1
#             if row[x]==0 or col[y]==0: return i
        
#         return -1

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m,n,res=len(mat),len(mat[0]),inf

        val2ind={x:i for i,x in enumerate(arr)}
        for i in range(m):
            for j in range(n):
                mat[i][j]=val2ind[mat[i][j]]
            res=min(res,max(mat[i]))
        
        for j in range(n):
            mx=max(mat[i][j] for i in range(m))
            res=min(res,mx)
        
        return res