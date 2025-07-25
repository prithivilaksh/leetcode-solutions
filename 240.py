# class Solution:
#     def searchMatrix(self, mat: List[List[int]], t: int) -> bool:
        
#         m,n=len(mat),len(mat[0])
        
#         for i in range(m):
#             l,r=0,n-1
#             if t<mat[i][l] or t>mat[i][r]: continue
#             while l<=r:
#                 m=l+(r-l)//2
#                 if mat[i][m]==t: return True
#                 elif mat[i][m]<t: l=m+1
#                 else: r=m-1

#         return False


# class Solution:
#     def searchMatrix(self, mat: List[List[int]], t: int) -> bool:
        
#         m,n=len(mat),len(mat[0])
#         r,c=m-1,0
#         while r>=0 and c<n:
#             if mat[r][c]==t: return True
#             elif mat[r][c]<t: c+=1
#             else: r-=1
#         return False


class Solution:
    def searchMatrix(self, mat: List[List[int]], t: int) -> bool:
        
        m,n=len(mat),len(mat[0])
        r,c=0,n-1
        while r<m and c>=0:
            if mat[r][c]==t: return True
            elif mat[r][c]<t: r+=1
            else: c-=1
        return False

        

