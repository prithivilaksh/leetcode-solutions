# class Solution:
#     def largestVariance(self, s: str) -> int:
        
#         n,res=len(s),0

#         for i in range(n):
#             cnt=defaultdict(int)
#             for j in range(i,n):
#                 cnt[s[j]]+=1
#                 mi,mx=inf,0
#                 for v in cnt.values():
#                     mi=min(mi,v)
#                     mx=max(mx,v)
#                 res=max(res,mx-mi)
#         return res


class Solution:
    def largestVariance(self, s: str) -> int:
        
        chars=list(set(s))
        m,n,res=len(chars),len(s),0

        def find_var(a,b):
            res=rsum=0
            hasb=lastb=False
            for c in s:
                if c not in (a,b): continue
                x= 1 if c==a else -1
                if rsum+x>=0:
                    rsum+=x
                    hasb= hasb or c==b
                    
                else: 
                    rsum=0
                    lastb= c==b
                    hasb=False
                    

                if hasb: res=max(res,rsum)
                elif lastb: res=max(res,rsum-1)
            return res
                

        for i in range(m):
            for j in range(i+1,m):
                a,b=chars[i],chars[j]
                res=max(res,find_var(a,b),find_var(b,a))
        return res
