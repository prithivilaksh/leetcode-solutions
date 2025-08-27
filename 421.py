class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # observation:
        #     - 2 ^ x requires x+1 bits
        #     - (2 ^ x)-1 requires x bits => we need to process 31 bits [0,30]
        #     - process bit by bit from left to right (MSB)
        #     - greedily check for a given prefix if its counterpart exists in the prefix set
        #     - if a^b=c then a^c=b and b^c=a

        res=0
        for i in range(30,-1,-1):
            res=res<<1 # <pres>0
            want=res|1 # <pres>1
            pre={x>>i for x in nums}
            for p in pre:
                if p^want in pre:
                    res=want;break
        
        return res


# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
        
#         # observation:
#         #     - 2 ^ x requires x+1 bits
#         #     - (2 ^ x)-1 requires x bits => we need to process 31 bits [0,30]
#         #     - process bit by bit from left to right (MSB)
#         #     - greedily check for a given prefix if its counter part exists in the prefix set
#         #     - if a^b=c then a^c=b and b^c=a

#         res=0
#         for i in range(30,-1,-1):
#             res=res<<1 # <pres>0
#             want=res|1 # <pres>1
#             pre={x>>i for x in nums}
#             for p in pre:
#                 if p^want in pre:
#                     res=want;break
#             nums=set(filter(lambda x: (x>>i)^res in pre,nums)) #not really required but good optimization for large n
        
#         return res
