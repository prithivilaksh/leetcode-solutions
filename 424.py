# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         cnt=defaultdict(int)
#         i=res=0
#         for j,c in enumerate(s):
#             cnt[c]+=1
#             mx=max(cnt.values())
#             if j-i+1-mx<=k: res=max(res,j-i+1)
#             else:
#                 cnt[s[i]]-=1
#                 i+=1
#         return res


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         cnt=defaultdict(int)
#         i=0
#         for j,c in enumerate(s):
#             cnt[c]+=1
#             mx=max(cnt.values())
#             if j-i+1-mx>k:
#                 cnt[s[i]]-=1
#                 i+=1
#         return j-i+1


# k=1
# A A A AAAAAAABBAAA

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt=defaultdict(int)
        i=mx=0
        for j,c in enumerate(s):
            cnt[c]+=1
            mx=max(mx,cnt[c])
            if j-i+1-mx>k:
                cnt[s[i]]-=1
                i+=1
        return j-i+1