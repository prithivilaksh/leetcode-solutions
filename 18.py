# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         # note:
#         #     1) a,b,c,d are unique
#         #     2) return unique [nums[a],nums[b],nums[c],nums[d]]
#         #     3) [nums[a],nums[b],nums[c],nums[d]] = [nums[d],nums[c],nums[a],nums[b]]

#         nums.sort()
#         n,res=len(nums),[]
#         for a in range(n):
#             if a>0 and nums[a-1]==nums[a]: continue
#             for b in range(a+1,n):
#                 if b>a+1 and nums[b-1]==nums[b]: continue
#                 for c in range(b+1,n):
#                     if c>b+1 and nums[c-1]==nums[c]: continue
#                     for d in range(c+1,n):
#                         if d>c+1 and nums[d-1]==nums[d]: continue
#                         if nums[a]+nums[b]+nums[c]+nums[d]>target: break
#                         if nums[a]+nums[b]+nums[c]+nums[d]==target:
#                             res.append((nums[a],nums[b],nums[c],nums[d]))
#         return res


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         # note:
#         #     1) a,b,c,d are unique
#         #     2) return unique [nums[a],nums[b],nums[c],nums[d]]
#         #     3) [nums[a],nums[b],nums[c],nums[d]] = [nums[d],nums[c],nums[a],nums[b]]

#         nums.sort()
#         n,res=len(nums),[]
#         for a in range(n):
#             if a>0 and nums[a-1]==nums[a]: continue
#             for b in range(a+1,n):
#                 if b>a+1 and nums[b-1]==nums[b]: continue
#                 c,d=b+1,n-1
#                 while c<d:
#                     if c>b+1 and nums[c-1]==nums[c]: c+=1
#                     elif d<n-1 and nums[d]==nums[d+1]: d-=1
#                     elif nums[a]+nums[b]+nums[c]+nums[d]==target: 
#                         res.append((nums[a],nums[b],nums[c],nums[d]))
#                         c+=1;d-=1
#                     elif nums[a]+nums[b]+nums[c]+nums[d]>target:d-=1
#                     else: c+=1
#         return res


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         # note:
#         #     1) a,b,c,d are unique
#         #     2) return unique [nums[a],nums[b],nums[c],nums[d]]
#         #     3) [nums[a],nums[b],nums[c],nums[d]] = [nums[d],nums[c],nums[a],nums[b]]

#         nums.sort()
#         n,res=len(nums),[]
#         for a in range(n):
#             if a!=0 and nums[a-1]==nums[a]: continue
#             for b in range(a+1,n):
#                 if b!=a+1 and nums[b-1]==nums[b]: continue
#                 c,d=b+1,n-1
#                 while c<d:
#                     total=nums[a]+nums[b]+nums[c]+nums[d]
#                     if (c!=b+1 and nums[c-1]==nums[c]) or total<target: c+=1
#                     elif (d!=n-1 and nums[d]==nums[d+1]) or total>target: d-=1
#                     else : 
#                         res.append((nums[a],nums[b],nums[c],nums[d]))
#                         c+=1;d-=1
#         return res


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         # note:
#         #     1) a,b,c,d are unique
#         #     2) return unique [nums[a],nums[b],nums[c],nums[d]]
#         #     3) [nums[a],nums[b],nums[c],nums[d]] = [nums[d],nums[c],nums[a],nums[b]]

#         nums.sort()
#         n,res=len(nums),[]
#         for a in range(n):
#             if a!=0 and nums[a-1]==nums[a]: continue
#             for b in range(a+1,n):
#                 if b!=a+1 and nums[b-1]==nums[b]: continue
#                 c,d=b+1,n-1
#                 while c<d:
#                     total=nums[a]+nums[b]+nums[c]+nums[d]
#                     if total<target: c+=1
#                     elif total>target: d-=1
#                     else : 
#                         res.append((nums[a],nums[b],nums[c],nums[d]))
#                         c+=1;d-=1
#                         while c<d and nums[c-1]==nums[c]:c+=1
#                         while c<d and nums[d]==nums[d+1]:d-=1
#         return res


class Solution:
    def fourSum(self, nums: List[int], t: int) -> List[List[int]]:
        
        # note:
        #     1) a,b,c,d are unique
        #     2) return unique [nums[a],nums[b],nums[c],nums[d]]
        #     3) [nums[a],nums[b],nums[c],nums[d]] = [nums[d],nums[c],nums[a],nums[b]]

        res=[]
        def kSum(l,r,t,k,ires):
            if r-l+1<k or nums[l]*k>t or nums[r]*k<t: return

            if k==2:
                while l<r:
                    tot=nums[l]+nums[r]
                    if tot<t: l+=1
                    elif tot>t: r-=1
                    else:
                        res.append(ires+[nums[l],nums[r]])
                        l+=1;r-=1
                        while l<r and nums[l-1]==nums[l]: l+=1
                        while l<r and nums[r]==nums[r+1]: r-=1
            else:
                for i in range(l,r+1):
                    if i!=l and nums[i-1]==nums[i]: continue
                    kSum(i+1,r,t-nums[i],k-1,ires+[nums[i]])
        nums.sort()
        kSum(0,len(nums)-1,t,4,[])
        return res