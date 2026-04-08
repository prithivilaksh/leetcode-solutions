# class Solution:
#     def furthestBuilding(self, ht: List[int], b: int, l: int) -> int:
        
#         n,h=len(ht),[]
#         for i in range(n-1):
#             if ht[i]>=ht[i+1]: continue

#             need=ht[i+1]-ht[i]
#             heappush(h,-need)
#             b-=need

#             while b<0 and h and l:
#                 b+=-heappop(h)
#                 l-=1
            
#             if b<0: return i
            
#         return n-1

class Solution:
    def furthestBuilding(self, ht: List[int], b: int, l: int) -> int:
        
        n,h=len(ht),[]
        for i in range(n-1):
            if ht[i]>=ht[i+1]: continue

            need=ht[i+1]-ht[i]
            heappush(h,-need)
            b-=need

            if b<0:
                if not l: return i
                b+=-heappop(h)
                l-=1
                        
        return n-1