class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        
        @cache
        def dp(i,j):
            res,x=0,mat[i][j]
            if i+1<m and mat[i+1][j]>x: res=max(res,dp(i+1,j))        
            if i-1>=0 and mat[i-1][j]>x: res=max(res,dp(i-1,j))        
            if j+1<n and mat[i][j+1]>x: res=max(res,dp(i,j+1))        
            if j-1>=0 and mat[i][j-1]>x: res=max(res,dp(i,j-1))  
            return 1+res      

        m,n,res=len(mat),len(mat[0]),0
        for i in range(m):
            for j in range(n):
                    res=max(res,dp(i,j))
        return res
