# class Solution:
#     def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        
#         m,n=len(mat),len(mat[0])
#         @cache
#         def dp(i,j):
#             if i==m or j==n: return inf
#             if i==m-1 and j==n-1:
#                 if mat[i][j]<=0: return -mat[i][j]
#                 else: return 0
            
#             req1=dp(i+1,j)
#             req2=dp(i,j+1)
#             reqnext=min(req1,req2)
#             if mat[i][j]<=0: return -mat[i][j]+reqnext
#             return max(0,reqnext-mat[i][j])
        
#         return dp(0,0)+1
            

# class Solution:
#     def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        
#         m,n=len(mat),len(mat[0])
#         @cache
#         def dp(i,j):
#             if i==m or j==n: return inf
#             if i==m-1 and j==n-1: return max(0,-mat[i][j])
            
#             next=min(dp(i+1,j),dp(i,j+1))
#             return max(0,-mat[i][j]+next)
        
#         return dp(0,0)+1

# class Solution:
#     def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        
#         m,n=len(mat),len(mat[0])
#         @cache
#         def dp(i,j):
#             if i==m or j==n: return inf
#             if i==m-1 and j==n-1: return max(0,-mat[i][j])
            
#             next=min(dp(i+1,j),dp(i,j+1))
#             return max(0,-mat[i][j]+next)
        
#         return dp(0,0)+1

class Solution:
    def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        
        m,n=len(mat),len(mat[0])
        @cache
        def dp(i,j):
            if i==m or j==n: return -inf
            if i==m-1 and j==n-1: return min(0,mat[i][j])
            
            next=max(dp(i+1,j),dp(i,j+1))
            return min(0,mat[i][j]+next)
        
        return -dp(0,0)+1
            