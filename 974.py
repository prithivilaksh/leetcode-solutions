class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        mp=[0]*k
        mp[0]=1
        s=res=0
        for x in nums:
            s+=x
            res+=mp[s%k]
            mp[s%k]+=1

        return res
