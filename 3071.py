class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        ycnt=defaultdict(int)
        rcnt=defaultdict(int)

        n=len(grid)
        for i in range(n):
            for j in range(n):
                if (i==j and i<=n//2) or (j==n//2 and i>=n//2) or (i<j and i+j==n-1):
                    ycnt[grid[i][j]]+=1
                else: rcnt[grid[i][j]]+=1
        
        y=n+(n//2)
        r=(n*n)-y

        ops0=y-ycnt[0]+min(rcnt[0]+rcnt[1],rcnt[0]+rcnt[2])
        ops1=y-ycnt[1]+min(rcnt[1]+rcnt[0],rcnt[1]+rcnt[2])
        ops2=y-ycnt[2]+min(rcnt[2]+rcnt[1],rcnt[2]+rcnt[0])

        return min(ops0,ops1,ops2)