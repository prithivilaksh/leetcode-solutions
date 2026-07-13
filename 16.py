# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
        
#         nums.sort()
#         n=len(nums)
#         mindiff,res=inf,None
#         for i in range(n):
#             for j in range(i+1,n):
#                 t=target-nums[i]-nums[j]
#                 r=bisect_right(nums,t,lo=j+1)
#                 l=r-1
#                 for pos in (l,r):
#                     if pos==j or pos==n: continue
#                     if abs(t-nums[pos])<mindiff:
#                         mindiff=abs(t-nums[pos])
#                         res=nums[i]+nums[j]+nums[pos]
#         return res


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
        
#         nums.sort()
#         n=len(nums)
#         mindiff,res=inf,None
#         for i in range(n):
#             if i-1>=0 and nums[i-1]==nums[i]: continue
#             for j in range(i+1,n):
#                 if j-1>i and nums[j-1]==nums[j]: continue
#                 t=target-nums[i]-nums[j]
#                 r=bisect_right(nums,t,lo=j+1)
#                 l=r-1
#                 for pos in (l,r):
#                     if pos==j or pos==n: continue
#                     if abs(t-nums[pos])<mindiff:
#                         mindiff=abs(t-nums[pos])
#                         res=nums[i]+nums[j]+nums[pos]
#         return res


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n,mindiff,res=len(nums),inf,None
        
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]: continue

            t=target-nums[i]
            j,k=i+1,n-1

            if nums[j]+nums[j+1]>=t: 
                if abs(t-nums[j]-nums[j+1])<mindiff:
                    mindiff=abs(t-nums[j]-nums[j+1])
                    res=nums[i]+nums[j]+nums[j+1]
                return res

            if nums[k-1]+nums[k]<=t:
                if abs(t-nums[k-1]-nums[k])<mindiff:
                    mindiff=abs(t-nums[k-1]-nums[k])
                    res=nums[i]+nums[k-1]+nums[k]
                continue
            
            while j<k:
                if abs(t-nums[j]-nums[k])<mindiff:
                    mindiff=abs(t-nums[j]-nums[k])
                    res=nums[i]+nums[j]+nums[k]
                if t-nums[j]-nums[k]<0: k-=1
                else: j+=1
            
            if mindiff==0: break
        return res


# class Solution:
#     def threeSumClosest(self, nums: list[int], target: int) -> int:
#         nums.sort()
#         n, min_diff, best = len(nums), float('inf'), 0
        
#         for i in range(n - 2):
#             if i and nums[i] == nums[i-1]: continue
#             x = nums[i]
            
#             # 🚀 Bound 1: Smallest possible sum is already too large
#             if (s_min := x + nums[i+1] + nums[i+2]) >= target:
#                 print("a")
#                 return s_min if s_min - target < min_diff else best
            
#             # 🚀 Bound 2: Largest possible sum is too small
#             if (s_max := x + nums[-2] + nums[-1]) <= target:
#                 if target - s_max < min_diff:
#                     min_diff, best = target - s_max, s_max
#                 print("b")
#                 continue # Skip the inner loop, we maxed out this 'i'
            
#             # Your sexy two-pointer scan for what's left
#             j, k, newt = i+1, n-1, target-x
#             while min_diff and j < k:
#                 if (diff := abs(newt - (c_sum := nums[j] + nums[k]))) < min_diff:
#                     min_diff, best = diff, x + c_sum
#                     print("c")
#                 if c_sum > newt: k -= 1
#                 else: j += 1
                
#         return best