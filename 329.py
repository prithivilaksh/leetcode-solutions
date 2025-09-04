class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        
        m,n=len(mat),len(mat[0])

        @cache
        def dp(i,j):
            res=0
            val=mat[i][j]
            mat[i][j]=-1
            if i+1<m and val<mat[i+1][j]:res=max(res,dp(i+1,j))
            if i-1>=0 and val<mat[i-1][j]:res=max(res,dp(i-1,j))
            if j+1<n and val<mat[i][j+1]:res=max(res,dp(i,j+1))
            if j-1>=0 and val<mat[i][j-1]:res=max(res,dp(i,j-1))
            mat[i][j]=val
            return res+1
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,dp(i,j))
        return res