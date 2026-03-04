# # MLE

# class Solution:
#     def distinctSubseqII(self, s: str) -> int:
        
#         n,st=len(s),set([""])
#         for i in range(n-1,-1,-1):
#             tst=set()
#             for x in st:
#                 tst.add(s[i]+x)
#             st.update(tst)
#         return (len(st)-1)%(10**9+7)


class Solution:
    def distinctSubseqII(self, s: str) -> int:

        # idea/obs:
        # 1) let dp[i] denote number of distinct subsequences from i..end
        # 2) dp[i] = dp[i+1] + dp[i+1] - number of distinct subsequences from i+1 which starts with s[i] 
        # 3) e.g. abac

        #         ''
        #         c

        #         a
        #         ac

        #         b
        #         bc
        #         ba
        #         bac

        #         a
        #         ac
        #         aa
        #         aac
        #         ab
        #         abc
        #         aba
        #         abac
        m=10**9+7
        cnt=defaultdict(int)
        n=len(s)
        dp=[0]*(n+1)
        dp[n]=1
        for i in range(n-1,-1,-1):
            dp[i]=(dp[i+1]+dp[i+1]-cnt[s[i]])%m
            cnt[s[i]]=(cnt[s[i]]+dp[i+1]-cnt[s[i]])%m
        
        return (dp[0]-1)%m


# class Solution:
#     def distinctSubseqII(self, s: str) -> int:

#         # idea/obs:
#         # 1) let dp[i] denote number of distinct subsequences from i..end
#         # 2) dp[i] = dp[i+1] + dp[i+1] - number of distinct subsequences from i+1 which starts with s[i] 
#         # 3) e.g. abac

#         #         ''
#         #         c

#         #         a
#         #         ac

#         #         b
#         #         bc
#         #         ba
#         #         bac

#         #         a
#         #         ac
#         #         aa
#         #         aac
#         #         ab
#         #         abc
#         #         aba
#         #         abac
#         m=10**9+7
#         cnt=defaultdict(int)
#         n=len(s)
#         dpnext=1
#         for i in range(n-1,-1,-1):
#             dpcurr=(2*dpnext-cnt[s[i]])%m
#             cnt[s[i]]=dpnext%m
#             dpnext=dpcurr
        
#         return (dpnext-1)%m