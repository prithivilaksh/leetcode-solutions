# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         # idea/observation:
#         #     1) For a valid triangle a+b>c where 0<a<=b<=c
#         n,res=len(nums),0
#         for i in range(n):
#             if nums[i]==0: continue
#             for j in range(i+1,n):
#                 if nums[j]==0: continue
#                 for k in range(j+1,n):
#                     if nums[k]==0: continue
#                     mx=max(nums[i],nums[j],nums[k])
#                     tot=nums[i]+nums[j]+nums[k]
#                     if tot-mx>mx: res+=1
#         return res

# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         # idea/observation:
#         #     1) For a valid triangle a+b>c where 0<a<=b<=c
#         nums.sort()
#         n,res=len(nums),0
        
#         for i in range(n):
#             for j in range(i+1,n):
#                 k=bisect_left(nums,nums[i]+nums[j])-1
#                 res+=max(0,k-j)
#         return res

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # idea/observation:
        #     1) For a valid triangle a+b>c where 0<a<=b<=c
        nums.sort()
        n,res=len(nums),0
        
        for k in range(n-1,-1,-1):
            l,r=0,k-1
            while l<r:
                if nums[l]+nums[r]>nums[k]:
                    res+=r-l
                    r-=1
                else: l+=1
        return res
