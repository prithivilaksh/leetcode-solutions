class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        tot=sum(nums)
        if tot%4!=0: return False
        nums.sort(reverse=True)
        t=tot//4
        n=len(nums)
        if nums[0]>t: return False

        def backtrack(pos,rem,s):
            if s==t: pos,rem,s=0,rem-1,0
            if rem==1: return True
            for i in range(pos,n):
                if pos<i and nums[i-1]==nums[i]: continue
                if nums[i]>=1 and s+nums[i]<=t:
                    nums[i]=-nums[i]
                    if backtrack(i+1,rem,s-nums[i]): return True
                    nums[i]=-nums[i]
                    if s==0 or s+nums[i]==t: return False
            return False
        return backtrack(0,4,0)

