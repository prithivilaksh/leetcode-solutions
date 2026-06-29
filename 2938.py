# class Solution:
#     def minimumSteps(self, s: str) -> int:
        
#         n,zeros,res=len(s),0,0
#         for i in range(n-1,-1,-1):
#             if s[i]=='0': zeros+=1
#             else: res+=zeros
#         return res


class Solution:
    def minimumSteps(self, s: str) -> int:
        
        zeros=res=0
        for x in s[::-1]:
            if x=='0': zeros+=1
            else: res+=zeros
        return res