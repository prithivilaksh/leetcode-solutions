# class Solution:
#     def findGCD(self, nums: List[int]) -> int:
#         def gcd(a,b): 
#             if b==0: return a
#             return gcd(b,a%b)
#         return gcd(min(nums),max(nums))

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b): 
            while b:
                a,b=b,a%b
            return a
        return gcd(min(nums),max(nums))