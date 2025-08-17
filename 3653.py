class Solution:
    # has a better solution 3655
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        MOD=10**9+7
        for l,r,k,v in queries:
            for i in range(l,r+1,k):
                nums[i]=(nums[i]*v) % MOD

        return reduce(lambda x,y: x^y,nums)

