# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
#         n=len(scores)
#         agsc=sorted(zip(ages,scores))

#         @cache
#         def dp(i, mxscore):
#             if i==n: return 0
#             res=dp(i+1,mxscore)
#             if mxscore<=agsc[i][1]:
#                 res=max(res,agsc[i][1]+dp(i+1,agsc[i][1]))
#             return res
        
#         return dp(0,0)

# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
#         n=len(scores)
#         agsc=sorted(zip(ages,scores))

#         @cache
#         def dp(i):
#             res=agsc[i][1]
#             for j in range(i+1,n):
#                 if agsc[i][1]<=agsc[j][1]:
#                     res=max(res,agsc[i][1]+dp(j))
#             return res
        
#         return max(dp(i) for i in range(n))

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        dp = [0]*(1+max(ages))    
        score_age = sorted(zip(scores, ages))
        for score, age in score_age:
            dp[age] = score + max(dp[:age+1])
        return max(dp)  