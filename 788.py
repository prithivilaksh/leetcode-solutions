# class Solution:
#     def rotatedDigits(self, N):
#         s1={0,1,8, 2,5,6,9}
#         s2={0,1,8}
#         res,past=0,set()
#         N=list(map(int,str(N)))
#         for i,n in enumerate(N):
#             for x in range(n):
#                 if x in s1: res+=7**(len(N)-1-i)
#                 if past.issubset(s2) and x in s2: res-=3**(len(N)-1-i)
#             if n not in s1: return res
#             past.add(n)
#         return res+ (not past.issubset(s2))

class Solution:
    def rotatedDigits(self, N):
        N=list(map(int,str(N)))
        vals=(0,1,2,5,6,8,9)
        s={0,1,8}

        @cache
        def dp(pos,strict,good):
            if pos==len(N): return good

            up = N[pos] if strict else 10
            res=0
            for x in vals:
                if x>up: break
                res+=dp(pos+1,x==up,True if x not in s else good)
            return res

        return dp(0,True,False)
