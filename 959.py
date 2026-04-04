# class Solution:
#     def regionsBySlashes(self, grid: List[str]) -> int:
        
#         def find(x):
#             if x!=par[x]:
#                 par[x]=find(par[x])
#             return par[x]
        
#         def union(a,b):
#             a,b=find(a),find(b)
#             par[a]=b
        
#         n=len(grid)
#         par={}
#         for i in range(n):
#             for j in range(n):
#                 t,b,l,r=(i,j,1),(i,j,2),(i,j,3),(i,j,4)
#                 for x in (t,b,l,r): par[x]=x
#                 if grid[i][j]=='/':
#                     union(t,l);union(b,r)
#                 elif grid[i][j]=='\\':
#                     union(t,r);union(b,l)
#                 else:
#                     union(t,l);union(t,b);union(t,r)
                
#                 if i-1>=0: union(t,(i-1,j,2))
#                 if j-1>=0: union(l,(i,j-1,4))

#         return sum(k==v for k,v in par.items())

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if x!=par[x]:
                par[x]=find(par[x])
            return par[x]
        
        def union(a,b):
            a,b=find(a),find(b)
            if a!=b: count[0]-=1
            par[a]=b
        
        n=len(grid)
        count=[n*n*4]
        par={}
        for i in range(n):
            for j in range(n):
                t,b,l,r=(i,j,1),(i,j,2),(i,j,3),(i,j,4)
                for x in (t,b,l,r): par[x]=x
                if grid[i][j]=='/':
                    union(t,l);union(b,r)
                elif grid[i][j]=='\\':
                    union(t,r);union(b,l)
                else:
                    union(t,l);union(t,b);union(t,r)
                
                if i-1>=0: union(t,(i-1,j,2))
                if j-1>=0: union(l,(i,j-1,4))

        return count[0]