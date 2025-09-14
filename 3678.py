class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:

        # observation:
        #     if avg=4, start=5
        #     if avg=4.5, start=5
        #     if avg=4.99, start=5

        n=len(nums)
        avg=sum(nums)//n
        res=max(1,avg+1)
        nums=set(nums)
        while res in nums: res+=1
        return res
        