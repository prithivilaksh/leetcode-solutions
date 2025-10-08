# from collections import defaultdict
# class Solution:
#     def equalDigitFrequency(self, s: str) -> int:

#         n,res=len(s),set()
#         for i in range(n):
#             char2cnt=defaultdict(int)
#             charcnt2cnt=defaultdict(int)
#             uniqCnts=0
#             for j in range(i,n):
#                 c=s[j]
#                 char2cnt[c]+=1
#                 charcnt2cnt[char2cnt[c]-1]-=1
#                 if charcnt2cnt[char2cnt[c]-1]==0: uniqCnts-=1
#                 charcnt2cnt[char2cnt[c]]+=1
#                 if charcnt2cnt[char2cnt[c]]==1: uniqCnts+=1
#                 if uniqCnts==1: res.add(s[i:j+1])
                
#         return len(res)

## ------------------------------------------------------------------------


# from collections import defaultdict
# class Solution:
#     def equalDigitFrequency(self, s: str) -> int:

#         n,res=len(s),set()
#         for i in range(n):
#             cnt=defaultdict(int)
#             for j in range(i,n):
#                 cnt[s[j]]+=1
#                 if len(set(cnt.values()))==1: res.add(s[i:j+1])
                                
#         return len(res)

## ------------------------------------------------------------------------

from collections import defaultdict
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        m=10**9+7
        b=131
        n,res=len(s),set()
        for i in range(n):
            cnt=defaultdict(int)
            hash=0
            for j in range(i,n):
                cnt[s[j]]+=1
                hash=(hash*b+ord(s[j]))%m
                if len(set(cnt.values()))==1: res.add(hash)

        return len(res)


print(Solution().equalDigitFrequency("1212"))
print(Solution().equalDigitFrequency("12321"))



# Rolling Hash:
# m=10**9+7
# b=some large prime
# k=j-i+1
# 1)  H(s[i:j+1]) =   (s[i]*b**(k-1)   +   s[i+1]*b**(k-2) +...+   s[j]*b**0 )%m

# 2)  H(s[i+1:j+2])   =  (s[i+1]*b**(k-1)   +   s[i+2]*b**(k-2) +...+   s[j+1]*b**0 )%m

# rewriting 1) H(s[i:j+1]) -   s[i]*b**(k-1)  =   (s[i+1]*b**(k-2) +...+   s[j]*b**0 )%m
# multiplying by b: b*(H(s[i:j+1]) -   s[i]*b**(k-1))  =   (s[i+1]*b**(k-1) +...+   s[j]*b**1 )%m

# substituting in 2)  H(s[i+1:j+2])   =  (b*(H(s[i:j+1]) -   s[i]*b**(k-1)) +   s[j+1]*b**0 )%m