# class Solution:
#     def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:

#         m,n=len(grid),len(grid[0])

#         def rotate():
#             res=[[""]*m for i in range(n)]
#             for i in range(m):
#                 for j in range(n):
#                     res[j][m-1-i]=grid[i][j]
#             return res
        
#         for i in range(m):
#             pos=n-1
#             for j in range(n-1,-1,-1):
#                 if grid[i][j]=="*": pos=j-1
#                 elif grid[i][j]=="#": 
#                     grid[i][j]="."
#                     grid[i][pos]="#"
#                     pos-=1
        
        
#         return rotate()

class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:

        m,n=len(grid),len(grid[0])

        res=[["."]*m for i in range(n)]
        
        for i in range(m):
            pos=n-1
            for j in range(n-1,-1,-1):
                if grid[i][j]=="*": 
                    pos=j-1
                    res[j][m-1-i]="*"
                elif grid[i][j]=="#": 
                    res[pos][m-1-i]="#"
                    pos-=1
         
        return res