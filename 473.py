# class Solution:
#     def makesquare(self, nums: List[int]) -> bool:
#         tot=sum(nums)
#         if tot%4!=0: return False
#         nums.sort(reverse=True)
#         t=tot//4
#         n=len(nums)
#         if nums[0]>t: return False

#         def backtrack(pos,rem,s):
#             if s==t: pos,rem,s=0,rem-1,0
#             if rem==1: return True
#             for i in range(pos,n):
#                 if pos<i and nums[i-1]==nums[i]: continue
#                 if nums[i]>=1 and s+nums[i]<=t:
#                     nums[i]=-nums[i]
#                     if backtrack(i+1,rem,s-nums[i]): return True
#                     nums[i]=-nums[i]
#                     if s==0 or s+nums[i]==t: return False
#             return False
#         return backtrack(0,4,0)

class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        
        tot=sum(sticks)
        if tot%4!=0: return False
        tot,n=tot//4,len(sticks)
        sticks.sort(reverse=True)
        if sticks[0]>tot: return False

        def bt(pos,rem,tar):
            if tar==0: pos,rem,tar=0,rem-1,tot
            if rem==1: return True
            for i in range(pos,n):
                if i>pos and sticks[i-1]==sticks[i]: continue
                if sticks[i]<0 or sticks[i]>tar: continue
                sticks[i]=-sticks[i]
                if bt(i+1,rem,tar+sticks[i]): return True
                sticks[i]=-sticks[i]
                if tar==tot or tar==sticks[i]: return False
            return False
        
        return bt(0,4,tot)



