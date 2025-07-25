class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mp=defaultdict(int)
        s,res,mp[0]=0,0,1
        for x in nums:
            s+=x
            res+=mp[s-k]
            mp[s]+=1
        
        return res