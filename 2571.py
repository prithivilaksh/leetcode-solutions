# class Solution:
#     def minOperations(self, n: int) -> int:

#         pows = [1 << i for i in range(int(log2(n))+2)]
#         ops = 0

#         while n:
#             closest = min(pows, key=lambda p: abs(n-p))
#             n = abs(n-closest)
#             ops += 1

#         return ops


class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n&1 == 0:
                n >>= 1
            elif n&2:
                n += 1
                res += 1
            else:
                res += 1
                n >>= 2
        return res