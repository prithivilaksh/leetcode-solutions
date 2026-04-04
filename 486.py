# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
        
#         def backtrack(l,r):
#             if l==r: return nums[l]
            
#             res=0
#             p2=backtrack(l+1,r)
#             p1=nums[l]+sum(nums[l+1:r+1])-p2

#             res=max(res,p1)

#             p2=backtrack(l,r-1)
#             p1=nums[r]+sum(nums[l:r])-p2
#             res=max(res,p1)

#             return res
        
#         return backtrack(0,len(nums)-1)*2>=sum(nums)


# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
        
#         @cache
#         def dp(l,r):
#             if l==r: return nums[l]
#             res=0

#             p2=dp(l+1,r)
#             p1=nums[l]+sum(nums[l+1:r+1])-p2
#             res=max(res,p1)

#             p2=dp(l,r-1)
#             p1=nums[r]+sum(nums[l:r])-p2
#             res=max(res,p1)

#             return res
        
#         return dp(0,len(nums)-1)*2>=sum(nums)

# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
#         n=len(nums)
#         csum=nums[:]
#         for i in range(1,n):csum[i]+=csum[i-1]
#         @cache
#         def dp(l,r):
#             if l==r: return nums[l]
#             res=0

#             p2=dp(l+1,r)
#             p1=nums[l]+(csum[r]-csum[l+1]+nums[l+1])-p2
#             res=max(res,p1)

#             p2=dp(l,r-1)
#             p1=nums[r]+(csum[r-1]-csum[l]+nums[l])-p2
#             res=max(res,p1)

#             return res
        
#         return dp(0,n-1)*2>=csum[-1]

# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
        
#         @cache
#         def dp(p,l,r):
#             if l>r: return 0

#             if p:
#                 a=nums[l]+dp(0,l+1,r)
#                 b=nums[r]+dp(0,l,r-1)
#                 res=max(a,b)
#             else:
#                 a=-nums[l]+dp(1,l+1,r)
#                 b=-nums[r]+dp(1,l,r-1)
#                 res=min(a,b)

#             return res
        
#         return dp(1,0,len(nums)-1)>=0

# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
        
#         @cache
#         def score(l,r,player):
#             if l==r: return player*nums[l]
#             if player==1:
#                 return max(nums[l]+score(l+1,r,-1),nums[r]+score(l,r-1,-1))
#             else:
#                 return min(-nums[l]+score(l+1,r,1),-nums[r]+score(l,r-1,1))
        
#         return score(0,len(nums)-1,1)>=0

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def dp(l,r):
            if l==r: return nums[l]
            return max(nums[l]-dp(l+1,r),nums[r]-dp(l,r-1))
        
        return dp(0,len(nums)-1)>=0


























