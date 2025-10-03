class Solution:
    def splitArray(self, nums: List[int]) -> int:
        
        i,n=0,len(nums)
        while i+1<n and nums[i]<nums[i+1]: i+=1
        ind1=i
        if i+1<n and nums[i]==nums[i+1]:i+=1
        ind2=i
        while i+1<n and nums[i]>nums[i+1]: i+=1
        if i+1!=n: return -1
        if ind1==ind2:
            ind=ind1
            first=abs(sum(nums[:ind])-sum(nums[ind:]))
            second=abs(sum(nums[:ind+1])-sum(nums[ind+1:]))
            return min(first,second)
        return abs(sum(nums[:ind1+1])-sum(nums[ind2:]))
            

        