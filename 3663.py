# class Solution:
#     def getLeastFrequentDigit(self, n: int) -> int:

#         ncnt=defaultdict(int)
#         while n>0:
#             r=n%10
#             n=n//10
#             ncnt[r]+=1

#         res=(-1,10000000)
#         for i in range(10):
#             if ncnt[i]!=0 and ncnt[i]<res[1]:
#                 res=(i,ncnt[i])

#         return res[0]

# from collections import Counter
# class Solution:
#     def getLeastFrequentDigit(self, n: int) -> int:

#         n=str(n)
#         cnt=Counter(n)
#         res=[10,inf]
#         for v,c in cnt.items():
#             if c<res[1] or c==res[1] and int(v)<res[0]: 
#                 res=(int(v),c)

#         return res[0]

from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        n=str(n)
        cnt=Counter(n)
        return int(min(cnt,key=lambda k:(cnt[k],k))[0])