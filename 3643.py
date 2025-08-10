# class Solution:
#     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

#         for j in range(y,y+k):
#             t=x
#             b=x+k-1
#             while t<b:
#                 grid[t][j],grid[b][j]=grid[b][j],grid[t][j]
#                 t+=1;b-=1

#         return grid
                
# class Solution:
#     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
#         # swap corresponding rows within the k×k block
#         for i in range(k // 2):
#             top, bottom = x + i, x + k - 1 - i
#             grid[top][y : y + k], grid[bottom][y : y + k] = grid[bottom][y : y + k],grid[top][y : y + k]
#         return grid

                
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:


        t,b=x,x+k-1
        while t<b:
            grid[t][y:y+k],grid[b][y:y+k]=grid[b][y:y+k],grid[t][y:y+k]
            t+=1;b-=1
            
        return grid