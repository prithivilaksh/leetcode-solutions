# TLE
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         @cache
#         def dp(pos):
#             if pos==n-1: return nums[n-1]
#             res=-inf
#             for i in range(pos+1,min(n,pos+k+1)):
#                 res=max(res,dp(i))
#             return nums[pos]+res
#         return dp(0)

# TLE
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         @cache
#         def dp(pos):
#             if pos==n-1: return nums[n-1]
#             res=-inf
#             for i in range(pos+1,min(n,pos+k+1)):
#                 if nums[i]>=0:return nums[pos]+dp(i)
#                 res=max(res,dp(i))

#             return nums[pos]+res
#         return dp(0)


# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         h,mx=[],None
#         for i,x in enumerate(nums):
#             while h and h[0][1]<i-k:heappop(h)

#             mx=x+(-h[0][0] if h else 0)

#             heappush(h,(-mx,i))
        
#         return mx

# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         h,mx=[(-nums[0],0)],nums[0]
#         for i in range(1,n):
            
#             while h and h[0][1]<i-k:heappop(h)

#             mx=nums[i]+(-h[0][0])

#             heappush(h,(-mx,i))
        
#         return mx

# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         dq=deque()

#         for i,x in enumerate(nums):

#             if dq and dq[0][1]<i-k:dq.popleft()

#             mx=x+ (dq[0][0] if i!=0 else 0)

#             while dq and dq[-1][0]<=mx: dq.pop()
#             dq.append((mx,i))
        
#         return dq[-1][0]

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        dq=deque([(nums[0],0)])

        for i in range(1,n):
            if dq[0][1]<i-k:dq.popleft()
            mx=dq[0][0]+nums[i]
            while dq and dq[-1][0]<=mx: dq.pop()
            dq.append((mx,i))
        
        return dq[-1][0]



# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
        
#         n=len(nums)
#         dq=deque([(nums[0],0)])

#         for i in range(1,n):
#             mx=dq[0][0]+nums[i]
#             while dq and dq[-1][0]<=mx: dq.pop()
#             dq.append((mx,i))
#             if dq[0][1]<=i-k: dq.popleft()
        
#         return dq[-1][0]


# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
        
#         n=len(nums)
#         dq=deque([0])

#         for i in range(1,n):
#             nums[i]=nums[dq[0]]+nums[i]
#             while dq and nums[dq[-1]]<=nums[i]: dq.pop()
#             dq.append(i)
#             if dq[0]<=i-k: dq.popleft()
        
#         return nums[dq[-1]]

