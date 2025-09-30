class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
        
        
        # def bfs(i,j):
        #     q=[(i,j)]
        #     while(q):
        #         x,y=q.pop(0)
        #         if(x<0 or y<0 or x==len(grid) or y==len(grid[0]) or grid[x][y]!="1") : continue
        #         grid[x][y]="-1"
        #         q.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
        
        # res=0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if(grid[i][j]=="1"):
        #             res+=1
        #             bfs(i,j)
        # return res



        # def bfs(i,j):
        #     q=[(i,j)]
        #     while(q):
        #         x,y=q.pop(0)                
        #         if(x-1>=0 and grid[x-1][y]=="1"):grid[x-1][y]="-1",q.append((x-1,y))
        #         if(x+1<len(grid) and grid[x+1][y]=="1"):grid[x+1][y]="-1",q.append((x+1,y))
        #         if(y-1>=0 and grid[x][y-1]=="1"):grid[x][y-1]="-1",q.append((x,y-1))
        #         if(y+1<len(grid[0]) and grid[x][y+1]=="1"):grid[x][y+1]="-1",q.append((x,y+1))
        
        # res=0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if(grid[i][j]=="1"):
        #             res+=1
        #             grid[i][j]="-1"
        #             bfs(i,j)
        # return res

    def numIslands(self, grid: List[List[str]]) -> int:

            m,n,res=len(grid),len(grid[0]),0
            def dfs(i,j):
                grid[i][j]="0"
                if(i+1<m and grid[i+1][j]=="1"):dfs(i+1,j)
                if(i-1>=0 and grid[i-1][j]=="1"):dfs(i-1,j)
                if(j+1<n and grid[i][j+1]=="1"):dfs(i,j+1)
                if(j-1>=0 and grid[i][j-1]=="1"):dfs(i,j-1)
            
            # def bfs(i,j):
            #     q=deque([(i,j)])
            #     while q:
            #         i,j=q.popleft()
            #         grid[i][j]="0"
            #         if(i+1<m and grid[i+1][j]=="1"):grid[i+1][j]="0",q.append((i+1,j))
            #         if(i-1>=0 and grid[i-1][j]=="1"):grid[i-1][j]="0",q.append((i-1,j))
            #         if(j+1<n and grid[i][j+1]=="1"):grid[i][j+1]="0",q.append((i,j+1))
            #         if(j-1>=0 and grid[i][j-1]=="1"):grid[i][j-1]="0",q.append((i,j-1))
                    

            for i in range(m):
                for j in range(n):
                    if(grid[i][j]=="1"):
                        res+=1
                        dfs(i,j)
                        # bfs(i,j)
            return res






# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         m,n=len(grid),len(grid[0])
#         par,res=defaultdict(tuple),set()

#         def find(x):
#             if x !=par[x]:
#                 par[x]=find(par[x])
#             return par[x]

#         def union(a,b):
#             par[find(b)]=find(a)

#         for i in range(m):
#             for j in range(n):
#                 par[(i,j)]=(i,j)
#                 if grid[i][j]=="1":
#                     if i-1>=0 and grid[i-1][j]=="1": union((i-1,j),(i,j))
#                     if j-1>=0 and grid[i][j-1]=="1": union((i,j-1),(i,j))
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]=="1": res.add(find((i,j)))
#         return len(res)

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         m,n,res=len(grid),len(grid[0]),0
#         def dfs(i,j):
#             grid[i][j]=0
#             for vi,vj in ((i,j+1),(i,j-1),(i+1,j),(i-1,j)):
#                 if 0<=vi<m and 0<=vj<n and grid[vi][vj]=="1": dfs(vi,vj)
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]=="1":
#                     res+=1
#                     dfs(i,j)
#         return res























