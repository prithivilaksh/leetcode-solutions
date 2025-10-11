class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        
        l,r=max(w),sum(w)

        def check(wt):
            d,tot=1,0
            for x in w:
                if x+tot<=wt: tot+=x
                else: tot=x;d+=1
            return d<=days

        while l<r:
            m=l+(r-l)//2
            if check(m): r=m
            else: l=m+1
        return r


# class Solution:
#     def shipWithinDays(self, w: List[int], days: int) -> int:
        
#         l,r=max(w),sum(w)

#         def check(wt):
#             d,tot=1,0
#             for x in w:
#                 tot+=x
#                 if tot>wt: tot=x;d+=1
#             return d<=days

#         while l<r:
#             m=l+(r-l)//2
#             if check(m): r=m
#             else: l=m+1
#         return r
