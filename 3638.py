# class Solution:
#     def maxBalancedShipments(self, weight: List[int]) -> int:

#         res=mx=0
#         for i,x in enumerate(weight):
#             if x<mx:
#                 res+=1
#                 mx=0
#             else:
#                 mx=max(mx,x)

#         return res

class Solution:
    def maxBalancedShipments(self, w: List[int]) -> int:

        i,res,n=0,0,len(w)
        while i<n-1:
            if w[i]>w[i+1]:
                res+=1;i+=1
            i+=1

        return res