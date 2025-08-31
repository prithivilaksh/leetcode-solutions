class Solution:
    def score(self, A: List[str], X: str) -> int:
        # observations:
        #     - for every card, bucket it as per the left or right char which is different and the cards xx separately
        #     - for a given set left / right, the maximum pairs is based on the following
        #             3       
        #             3
        #         1   3       1
        #         1   2       1
        #         1   2       1
        #         1   2       1   2
        #         1   2       1   2
        #         1   2       1   2
        #     - if the max is <= tot//2, we can have tot//2 pairs, otherwise we can have tot-max pairs
        #     - after this we will have remaining from left/right and xx cards
        #     - after this if we have remaining xx cards, those can be used against exisiting pairs evenly.
        #     - for e.g if x=b and we have a pair ab,cb and bb,bb these can be paired like ab,bb and cb,bb
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