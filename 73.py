# class Solution:
#     def setZeroes(self, mat: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m,n=len(mat),len(mat[0])

#         isFirstZero=False
#         for j in range(n):
#             isFirstZero=isFirstZero or mat[0][j]==0

#         for i in range(1,m):
#             for j in range(n):
#                 if mat[i][j]==0:
#                     mat[0][j]=mat[i][0]=0
        
#         for i in range(m-1,0,-1):
#             for j in range(n-1,-1,-1):
#                 if mat[0][j]==0 or mat[i][0]==0:
#                     mat[i][j]=0
        
#         if isFirstZero:
#             for j in range(n):mat[0][j]=0
            

class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(mat),len(mat[0])

        isfrow0=any(mat[0][j]==0 for j in range(n))
        isfcol0=any(mat[i][0]==0 for i in range(m))

        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j]==0:
                    mat[0][j]=mat[i][0]=0
        
        for i in range(m-1,0,-1):
            for j in range(n-1,0,-1):
                if mat[0][j]==0 or mat[i][0]==0:
                    mat[i][j]=0
        
        if isfrow0:
            for j in range(n):mat[0][j]=0
        if isfcol0:
            for i in range(m):mat[i][0]=0
            