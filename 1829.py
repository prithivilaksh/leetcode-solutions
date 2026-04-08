# class Solution:
#     def getMaximumXor(self, nums: List[int], mxbit: int) -> List[int]:
        
#         res=[]
#         rxor,mx=0,2**mxbit-1
#         for x in nums:
#             rxor^=x
#             res.append(rxor^mx)
        
#         return res[::-1]

class Solution:
    def getMaximumXor(self, nums: List[int], mxbit: int) -> List[int]:
        
        res=[]
        rxor=2**mxbit-1
        for x in nums:
            rxor^=x
            res.append(rxor)
        
        return res[::-1]