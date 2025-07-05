# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
#         h=[]
#         for i,[x,y] in enumerate(points):
#             heapq.heappush(h,(x**2+y**2,i))
        
#         res=[]
#         for i in range(k):
#             pos=heapq.heappop(h)[1]
#             res.append(points[pos])
        
#         return res

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h=[]
        for i,[x,y] in enumerate(points):
            heapq.heappush(h,(-x**2-y**2,i))
            if len(h)==k+1: heapq.heappop(h)
        
    
        return [points[i] for _,i in h]