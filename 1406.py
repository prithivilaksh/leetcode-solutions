# class Solution:
#     def stoneGameIII(self, val: List[int]) -> str:
        
#         # idea:
#         # 1) let Alice=+, Bob=- and Tie=0

#         @cache
#         def dp(i):
#             if i==n: return 0
#             one=two=three=-inf
#             if i<n: one=val[i]-dp(i+1)
#             if i+1<n: two=val[i]+val[i+1]-dp(i+2)
#             if i+2<n: three=val[i]+val[i+1]+val[i+2]-dp(i+3)
#             return max(one,two,three)
#         n=len(val)
#         res=dp(0)
#         if res>0: return "Alice"
#         if res<0: return "Bob"
#         return "Tie"

class Solution:
    def stoneGameIII(self, val: List[int]) -> str:
        
        # idea:
        # 1) let Alice=+, Bob=- and Tie=0


        @cache
        def dp(i):
            if i==n: return 0
            
            if i+2<n: j=3
            elif i+1<n: j=2
            else: j=1

            res,rsum=-inf,0
            for k in range(j):
                rsum+=val[i+k]
                res=max(res,rsum-dp(i+k+1))
            return res

        n=len(val)
        res=dp(0)
        if res>0: return "Alice"
        if res<0: return "Bob"
        return "Tie"
        