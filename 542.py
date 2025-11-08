# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
#         m,n=len(mat),len(mat[0])
#         dq=deque()
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j]==0: dq.append((i,j))
#                 else: mat[i][j]=inf
#         d=1
#         while dq:
#             i,j=dq.popleft()
#             for vi,vj in ((i+1,j),(i,j+1),(i,j-1),(i-1,j)):
#                 if 0<=vi<m and 0<=vj<n and mat[vi][vj]==inf:
#                     mat[vi][vj]=mat[i][j]+1
#                     dq.append((vi,vj))
#         return mat

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m,n=len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]!=0:
                    mat[i][j]=inf
                    if i-1>=0: mat[i][j]=min(mat[i][j],mat[i-1][j]+1) 
                    if j-1>=0: mat[i][j]=min(mat[i][j],mat[i][j-1]+1) 
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j]!=0:
                    if i+1<m: mat[i][j]=min(mat[i][j],mat[i+1][j]+1) 
                    if j+1<n: mat[i][j]=min(mat[i][j],mat[i][j+1]+1) 
        return mat