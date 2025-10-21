# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         n,res=len(nums),0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if abs(nums[i]-nums[j])==k: res+=1
#         return res

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        # observation/idea:
        #     1) let nums[i]=x and nums[j]=y
        #     2) given x and y are +ve
        #     3) |x-y|==k
        #     4) => x-y=k => y=x-k
        #     5) => y-x=k => y=k+x
        
        res=0
        cnt=defaultdict(int)
        for x in nums: 
            res+=cnt[k+x]+cnt[x-k]
            cnt[x]+=1
        return res