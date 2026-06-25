# class Solution:

#     def totalNQueens(self, n: int) -> int:
        
#         mat=[[0]*n for _ in range(n)]

#         def filldown(r,c,delta):
#             mat[r][c]+=delta
#             y=1
#             for i in range(r+1,n):
#                 mat[i][c]+=delta
#                 if c-y>=0: mat[i][c-y]+=delta
#                 if c+y<n: mat[i][c+y]+=delta
#                 y+=1

#         def backtrack(q):
#             if q==n: return 1
#             res=0
#             for i in range(n):
#                 if mat[q][i]==0:
#                     filldown(q,i,1)
#                     res+=backtrack(q+1)
#                     filldown(q,i,-1)
#             return res

#         return backtrack(0)


class Solution:

    def totalNQueens(self, n: int) -> int:
        
        cols,ldia,rdia=set(),set(),set()

        def backtrack(r):
            if r==n: return 1
            res=0
            for c in range(n):
                if c in cols or c-r in ldia or c+r in rdia: continue
                cols.add(c);ldia.add(c-r);rdia.add(c+r)
                res+=backtrack(r+1)
                cols.remove(c);ldia.remove(c-r);rdia.remove(c+r)
            return res

        return backtrack(0)