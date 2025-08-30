class Solution:
    def score(self, A: List[str], X: str) -> int:
        both = 0
        l = defaultdict(int)
        r = defaultdict(int)
        for f,s in A:
            if f == s == X: both += 1
            elif f == X: r[s] += 1
            elif s == X: l[f] += 1

        pairs = rem = 0
        for count in [l.values(), r.values()]:
            tot = sum(count,0)
            mx = max(count,default=0)
            pnt = min(tot - mx, tot // 2)
            pairs += pnt
            rem += tot - 2 * pnt

        used = min(both, rem)
        both -= used
        extra = min(pairs, both // 2)
        return pairs + used + extra

# class Solution:
#     def score(self, A: List[str], X: str) -> int:
#         both = 0
#         l = defaultdict(int)
#         r = defaultdict(int)
#         for f,s in A:
#             if f == s == X: both += 1
#             elif f == X: r[s] += 1
#             elif s == X: l[f] += 1

#         ltot,lmax=sum(l.values(),0),max(l.values(),default=0)
#         rtot,rmax=sum(r.values(),0),max(r.values(),default=0)
#         res=0
#         for i in range(both+1):
#             j=both-i
#             tot1,max1=ltot+i,max(lmax,i)
#             tot2,max2=rtot+j,max(rmax,j)
#             pnt1,pnt2=min(tot1-max1,tot1//2),min(tot2-max2,tot2//2)
#             res=max(res,pnt1+pnt2)

#         return res