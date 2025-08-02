# class Solution:
#     def maximalSquare(self, mat: List[List[str]]) -> int:

#         m,n,res=len(mat),len(mat[0]),0
#         lr=[[0]*n for i in range(m)]
#         td=[[0]*n for i in range(m)]
        
#         for i in range(m):
#             for j in range(n):
#                 mat[i][j]=int(mat[i][j])
#                 if mat[i][j]:
#                     lr[i][j]=td[i][j]=mat[i][j]
#                     if j-1>=0: lr[i][j]+=lr[i][j-1]
#                     if i-1>=0: td[i][j]+=td[i-1][j]
#                     if i-1>=0 and j-1>=0:
#                         mat[i][j]=min(mat[i-1][j-1]+1,td[i][j],lr[i][j])
#                     res=max(res,mat[i][j])
        
#         return res*res

class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:

        m,n,res=len(mat),len(mat[0]),0
        for i in range(m):
            for j in range(n):
                mat[i][j]=int(mat[i][j])
                if mat[i][j]:
                    if i-1>=0 and j-1>=0:
                        mat[i][j]=min(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])+1
                    res=max(res,mat[i][j])
        
        return res*res