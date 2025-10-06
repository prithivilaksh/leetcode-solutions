# class Solution:
#     def kthFactor(self, n: int, k: int) -> int:
        
#         for i in range(1,n+1):
#             if n%i==0:
#                 k-=1
#                 if k==0: return i
        
#         return -1

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        for i in range(1,ceil(sqrt(n))):
            if n%i==0:
                k-=1
                if k==0: return i

        for i in range(floor(sqrt(n)),0,-1):
            if n%i==0:
                k-=1
                if k==0: return n//i
        
        return -1