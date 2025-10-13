class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for x in nums:
            pos=bisect_left(dp,x)
            if pos==len(dp): dp.append(x)
            else: dp[pos]=x
        return len(dp)
        
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         res,dp=1,[1]*n
#         for i in range(n-1,-1,-1):
#             for j in range(i+1,n):
#                 if nums[i]<nums[j]:
#                     dp[i]=max(dp[i],dp[j]+1)
#             res=max(res,dp[i])
#         return res

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         res=[]
#         for i in range(n):
#             pos=bisect_left(res,nums[i])
#             if pos==len(res): res.append(nums[i])
#             else: res[pos]=nums[i]

#         return len(res)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         map={x:i for i,x in enumerate(sorted(set(nums)))}
#         n=len(map)
#         f=[0]*(n+1)
#         def update(i,val):
#             i+=1
#             while i<=n:
#                 f[i]=max(f[i],val)
#                 i+=i&(-i)

#         def query(i):
#             i+=1
#             res=0
#             while i>0:
#                 res=max(res,f[i])
#                 i-=i&(-i)
#             return res

        
#         for x in nums:
#             i=map[x]
#             mx=query(i-1)
#             update(i,mx+1)

#         return query(n-1)

