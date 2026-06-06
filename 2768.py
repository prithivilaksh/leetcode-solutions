## TLE
# class Solution:
#     def countBlackBlocks(self, m: int, n: int, coords: List[List[int]]) -> List[int]:
        
#         coords=set((i,j) for i,j in coords)
#         res=[0]*5
#         for i in range(1,m):
#             for j in range(1,n):
#                 cnt=0
#                 for di,dj in (-1,-1),(-1,0),(0,-1),(0,0):
#                     x,y=i+di,j+dj
#                     cnt+=(x,y) in coords
#                 res[cnt]+=1
#         return res
                
class Solution:
    def countBlackBlocks(self, m: int, n: int, coords: List[List[int]]) -> List[int]:

        cnt,res=defaultdict(int),[0]*5
        for i,j in coords:
            for di,dj in (-1,-1),(-1,0),(0,-1),(0,0):
                x,y=i+di,j+dj
                if 0<=x<m-1 and 0<=y<n-1: cnt[(x,y)]+=1
        
        for c in cnt.values(): res[c]+=1
        res[0]=((m-1)*(n-1))-len(cnt)
        return res

                