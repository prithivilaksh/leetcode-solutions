# class Solution:
#     def canPlaceFlowers(self, fbed: List[int], n: int) -> bool:
        
#         m=len(fbed)
#         i=cnt=0
#         while i<m:
#             if fbed[i]==1: i+=2
#             elif i+1==m or (i+1<m and fbed[i+1]==0): cnt+=1;i+=2
#             else: i+=1
        
#         return cnt>=n

# class Solution:
#     def canPlaceFlowers(self, fbed: List[int], n: int) -> bool:
        
#         m=len(fbed)
#         i=cnt=0
#         while i<m:
#             if fbed[i]==1: i+=2
#             elif i+1==m or fbed[i+1]==0: cnt+=1;i+=2
#             else: i+=1
        
#         return cnt>=n

class Solution:
    def canPlaceFlowers(self, fbed: List[int], n: int) -> bool:
        
        m=len(fbed)
        for i in range(m):
            if fbed[i]==0 and (i==0 or fbed[i-1]==0) and (i==m-1 or fbed[i+1]==0):
                fbed[i]=1;n-=1
        
        return n<=0