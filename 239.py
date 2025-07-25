# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         n=len(nums)
#         h,res=[],[]
#         for r in range(n):
#             heappush(h,(-nums[r],r))
#             while len(h)>k and h[0][1]<=r-k:
#                 heappop(h)
#             if len(h)>=k:res.append(-h[0][0])
        
#         return res

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         n=len(nums)
#         h,res=[],[]
#         for r in range(n):
#             heappush(h,(-nums[r],r))
#             while h and h[0][1]<=r-k: heappop(h)
#             if r>=k-1:res.append(-h[0][0])
        
#         return res

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         n=len(nums)
#         lr,rl=[0]*n,[0]*n
#         res=[0]*(n-k+1)

#         for i in range(n):
#             if i==0 or i%k==0:lr[i]=nums[i]
#             else: lr[i]=max(lr[i-1],nums[i])
        
#         for i in range(n-1,-1,-1):
#             if i==n-1 or i%k==0:rl[i]=nums[i]
#             else: rl[i]=max(rl[i+1],nums[i])
        
#         for i in range(n-k+1):
#             res[i]=max(lr[i+k-1],rl[i])

#         return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        dq,res=deque(),[]
        for r in range(n):
            while dq and nums[dq[-1]]<=nums[r]:dq.pop()
            dq.append(r)
            if dq[0]<=r-k:dq.popleft()
            if r>=k-1: res.append(nums[dq[0]])
        
        return res