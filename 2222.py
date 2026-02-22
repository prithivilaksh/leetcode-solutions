# class Solution:
#     def numberOfWays(self, s: str) -> int:
        
#         n=len(s)
#         @cache
#         def dp(i,rem):
#             if rem==0: return 1
#             res=0
#             for j in range(i+1,n):
#                 if s[i]!=s[j]:
#                     res+=dp(j,rem-1)
#             return res
        
#         return sum(dp(i,2) for i in range(n))

class Solution:
    def numberOfWays(self, s: str) -> int:
        
        cnt=defaultdict(int)
        for c in s[::-1]:
            if c=="1": 
                cnt["101"]+=cnt["01"]
                cnt["10"]+=cnt["0"]
                cnt["1"]+=1
            else: 
                cnt["010"]+=cnt["10"]
                cnt["01"]+=cnt["1"]
                cnt["0"]+=1
        
        return cnt["010"]+cnt["101"]
            
