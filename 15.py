class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # idea/observation:
        #     -triplets-combination - (nums[i],nums[j],nums[k]) = (nums[j],nums[k],nums[i])
        #     -i!=j!=k
        #     -no duplicate triplets if nums[i+1]=nums[i] then (nums[i],nums[j],nums[k]) = (nums[i+1],nums[j],nums[k])

        res,n=[],len(nums)
        nums.sort()
        def kSum(k,t,ires,pos):
            if nums[pos]*k>t or nums[n-1]*k<t: return
            if k==2:
                l,r=pos,n-1
                while l<r:
                    tot=nums[l]+nums[r]
                    if tot==t:
                        res.append(ires+[nums[l],nums[r]])
                        l+=1;r-=1
                        while l<r and nums[l-1]==nums[l]:l+=1
                        while l<r and nums[r]==nums[r+1]:r-=1
                    elif tot<t: l+=1
                    else: r-=1
            else:
                for i in range(pos,n-k+1):
                    if i==pos or nums[i-1]!=nums[i]:
                        kSum(k-1,t-nums[i],ires+[nums[i]],i+1)
        
        kSum(3,0,[],0)
        return res