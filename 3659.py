class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        
        n=len(nums)
        if n%k!=0: return False

        grps=n//k
        cnt=defaultdict(int)
        for x in nums:
            cnt[x]+=1
            if cnt[x]>grps: return False

        return True