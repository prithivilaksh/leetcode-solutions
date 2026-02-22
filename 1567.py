# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
        
#         def max_len_lr(nums):
#             n,p,l,res=len(nums),1,0,0
#             for r in range(n):
#                 if nums[r]==0:
#                     p=1
#                     l=r+1
#                     continue
#                 p*=nums[r]
#                 if p>0: res=max(res,r-l+1)
#             return res
        
#         return max(max_len_lr(nums),max_len_lr(nums[::-1]))

# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
        
#         def max_len_lr(nums):
#             n,p,l,res=len(nums),1,0,0
#             for r in range(n):
#                 if nums[r]==0:
#                     p,l=1,r+1
#                     continue
#                 if nums[r]<0:p*=-1 
#                 if p>0: res=max(res,r-l+1)
#             return res
        
#         return max(max_len_lr(nums),max_len_lr(nums[::-1]))

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        res=p=n=0
        for i,x in enumerate(nums):
            if x==0: p=n=0
            elif x>0:
                p+=1
                n=0 if n==0 else n+1
            else:
                tp=p
                p=0 if n==0 else n+1
                n=tp+1
            res=max(res,p)
        return res
            

# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
        
#         def getMaxLenWithoutZero(l,r):
#             if l>r: return 0
#             if l==r: return int(nums[l]>0)

#             p,first,last=1,-1,-1
#             for i in range(l,r+1):
#                 p*=nums[i]
#                 if nums[i]<0:
#                     if first==-1: first=i
#                     last=i
            
#             if p>0: return r-l+1
#             return max(r-(first+1)+1,(last-1)-l+1)

#         nums.append(0)
#         res=l=0
#         for r in range(len(nums)):
#             if nums[r]==0:
#                 res=max(res,getMaxLenWithoutZero(l,r-1))
#                 l=r+1
        
#         return res            
