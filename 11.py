# class Solution:
#     def maxArea(self, h: List[int]) -> int:
        

#         l,r=0,len(h)-1
#         res=0
#         while l<r:
#             res=max(res,(r-l)*min(h[l],h[r]))
#             if h[l]<h[r]: l+=1
#             else: r-=1
        
#         return res

class Solution:
    def maxArea(self, h: List[int]) -> int:

        l,r=0,len(h)-1
        res=0
        while l<r:
            if h[l]<h[r]:
                res=max(res,(r-l)*h[l]) 
                l+=1
            else: 
                res=max(res,(r-l)*h[r])
                r-=1 
        return res


class Solution:
    def maxArea(self, h: List[int]) -> int:
        
        l,r,res=0,len(h)-1,0

        while l<r:
            res=max(res,(r-l)*min(h[l],h[r]))
            if h[l]<h[r]: l+=1
            else: r-=1
        return res

# class Solution:
#     def maxArea(self, h: List[int]) -> int:
        
#         l,r,res=0,len(h)-1,0
#         while l<r:
#             res=max(res,(r-l)*min(h[l],h[r]))
#             w=r-l
#             if h[l]<h[r]: 
#                 res=max(res,w*h[l])
#                 l+=1
#             else: 
#                 res=max(res,w*h[r])
#                 r-=1
#         return res