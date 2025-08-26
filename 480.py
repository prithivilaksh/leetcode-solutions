# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
#         l,r,res=[],[],[]

#         def rtol(x,i):
#             heappush(r,(x,i))
#             px,pi=heappop(r)
#             heappush(l,(-px,-pi))
        
#         def ltor(x,i):
#             heappush(l,(-x,-i))
#             px,pi=heappop(l)
#             heappush(r,(-px,-pi))

#         for i,x in enumerate(nums):
#             if i<=k-1:
#                 if len(l)<=len(r): rtol(x,i)
#                 else: ltor(x,i)
#             else:
#                 if nums[i-k]<=-l[0][0]: rtol(x,i)
#                 else: ltor(x,i)
                
#                 while -l[0][1]<=i-k:heappop(l)
#                 while r and r[0][1]<=i-k:heappop(r)
#             if i>=k-1:
#                 if k&1: res.append(-l[0][0])
#                 else: res.append((r[0][0]-l[0][0])/2)
#         return res



from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        sl=SortedList()
        res=[]
        for i,x in enumerate(nums):
            sl.add(x)
            if i>=k-1: 
                res.append(sl[k//2] if k&1 else (sl[k//2 -1]+sl[k//2])/2)
                sl.remove(nums[i-k+1])
        return res
        
        


