# class Solution:
#     def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
#         n=len(apples)
#         h,res,i=[],0,0
#         while h or i<n:
#             while h and h[0][0]<=i: heappop(h)

#             if i<n and apples[i]!=0: 
#                 heappush(h,(i+days[i],apples[i]))

#             if h:
#                 rt,avlbl=heappop(h)
#                 res+=1
#                 if avlbl!=1: heappush(h,(rt,avlbl-1))
#             i+=1
#         return res


# class Solution:
#     def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
#         n=len(apples)
#         h,res,i=[],0,0
#         while h or i<n:
#             while h and h[0][0]<=i: heappop(h)

#             if i<n and apples[i]!=0: 
#                 heappush(h,[i+days[i],apples[i]])

#             if h:
#                 h[0][1]-=1
#                 res+=1
#                 if h[0][1]==0: heappop(h)
#             i+=1
#         return res

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        n=len(apples)
        h,res,i=[],0,0
        for i in range(n):
            while h and h[0][0]<=i: heappop(h)

            if apples[i]: heappush(h,[i+days[i],apples[i]])

            if h:
                h[0][1]-=1
                res+=1
                if h[0][1]==0: heappop(h)
        i=n
        while h:
            rt,avlbl=heappop(h)
            mi=min(rt-i,avlbl)
            res+=mi
            i+=mi
        return res
