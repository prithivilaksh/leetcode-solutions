class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n,mins,cnt=len(grid),len(grid[0]),0,0
        dq=deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2: dq.append((i,j))
                elif grid[i][j]==1: cnt+=1
        
        while dq:
            for _ in range(len(dq)):
                i,j = dq.popleft()
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=x<m and 0<=y<n and grid[x][y]==1:
                        grid[x][y]=2;cnt-=1
                        dq.append((x,y))
            mins+=1
        
        return max(0,mins-1) if cnt==0 else -1