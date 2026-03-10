class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(t):
            rsum,cnt=0,1
            for x in nums:
                if rsum+x<=t: rsum+=x
                else:
                    rsum=x
                    cnt+=1
            return cnt<=k
        
        tot,mx=sum(nums),max(nums)
        l,r=mx,tot
        while l<r:
            m=l+(r-l)//2
            if check(m): r=m
            else: l=m+1
        return r