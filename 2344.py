# class Solution:
#     def minOperations(self, nums: List[int], nd: List[int]) -> int:
        
#         def gcd(a,b):
#             return a if b==0 else gcd(b,a%b)
        
#         ggcd,n=nd[0],len(nd)
#         for i in range(1,n):
#             ggcd=gcd(ggcd,nd[i])
        
#         res,cnt=0,Counter(nums)
#         for x in sorted(set(nums)):
#             if ggcd%x==0: break
#             res+=cnt[x]
        
#         return -1 if res==len(nums) else res

# class Solution:
#     def minOperations(self, nums: List[int], nd: List[int]) -> int:
        
#         def gcd(a,b):
#             return a if b==0 else gcd(b,a%b)
        
#         ggcd,n=nd[0],len(nd)
#         for i in range(1,n):
#             ggcd=gcd(ggcd,nd[i])
        
#         mi=inf
#         for x in set(nums):
#             if ggcd%x==0 and x<mi: mi=x
        
#         if mi==inf: return -1
        
#         res,cnt=0,Counter(nums)
#         for x,c in cnt.items():
#             if x<mi: res+=c
        
#         return res


# class Solution:
#     def minOperations(self, nums: List[int], nd: List[int]) -> int:
        
#         def gcd(a,b):
#             return a if b==0 else gcd(b,a%b)
        
#         ggcd,n=nd[0],len(nd)
#         for i in range(1,n):
#             ggcd=gcd(ggcd,nd[i])
        
#         mi=inf
#         for i,x in enumerate(sorted(nums)):
#             if ggcd%x==0: return i
#             if x>ggcd: return -1
        
#         return -1

class Solution:
    def minOperations(self, nums: List[int], nd: List[int]) -> int:
        
        ggcd=math.gcd(*nd)

        for i,x in enumerate(sorted(nums)):
            if ggcd%x==0: return i
            if x>ggcd: break
        
        return -1