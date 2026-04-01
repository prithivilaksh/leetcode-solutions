class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m,n=len(grid),len(grid[0])
        dq,d=deque([]),0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0: dq.append((i,j))
        
        while dq:
            for _ in range(len(dq)):
                i,j=dq.popleft()
                for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                    vi,vj=i+di,j+dj
                    if 0<=vi<m and 0<=vj<n and grid[vi][vj]==2147483647:
                        grid[vi][vj]=d+1
                        dq.append((vi,vj))
            d+=1

