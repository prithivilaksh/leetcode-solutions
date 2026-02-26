class Solution:
    def minSwaps(self, s: str) -> int:
        
        cnt=Counter(s)
        if abs(cnt["0"]-cnt["1"])>1: return -1

        def check(ss):
            cnt=0
            for i,c in enumerate(s):
                if c!=ss[i%2]: cnt+=1
            return cnt//2

        if cnt["0"]>cnt["1"]: return check("01")
        if cnt["0"]<cnt["1"]: return check("10")
        return min(check("01"),check("10"))
