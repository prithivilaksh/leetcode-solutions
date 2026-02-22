class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        
        mx=sum(x for x in nums if x>0)
        nums=sorted([abs(x) for x in nums])
        n=len(nums)
        h=[(-mx,0)]
        for _ in range(k-1):
            s,i=heappop(h)
            s=-s
            if i<n:
                heappush(h,(-(s-nums[i]),i+1))
                if i-1>=0: heappush(h,(-(s+nums[i-1]-nums[i]),i+1))

        return -h[0][0]
