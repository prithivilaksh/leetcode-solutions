# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         n,l,res=len(s),0,0
#         mp=defaultdict(int)
#         for r in range(n):
#             mp[s[r]]+=1
#             while mp[s[r]]>1:
#                 mp[s[l]]-=1
#                 l+=1
#             res=max(res,r-l+1)
#         return res

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         n,l,r,cnt=len(s),0,-1,0
#         mp=defaultdict(int)
#         for r in range(n):
#             mp[s[r]]+=1
#             if mp[s[r]]>1: cnt+=1
#             if cnt > 0:
#                 if mp[s[l]]!=1: cnt-=1
#                 mp[s[l]]-=1
#                 l+=1
#         return r-l+1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n,l,r,res=len(s),0,0,0
        mp=defaultdict(lambda:-1)

        for r in range(n):
            l=max(l,mp[s[r]]+1)
            mp[s[r]]=r
            res=max(res,r-l+1)

        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         cnt=defaultdict(int)
#         res=l=0
#         for r,c in enumerate(s):
#             cnt[c]+=1
#             while cnt[c]>1:
#                 cnt[s[l]]-=1
#                 l+=1
#             res=max(res,r-l+1)
#         return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cnt=defaultdict(int)
        res=l=more=0
        r=-1
        for r,c in enumerate(s):
            cnt[c]+=1
            if cnt[c]==2: more+=1
            if more>=1:
                if cnt[s[l]]==2: more-=1
                cnt[s[l]]-=1
                l+=1
        return r-l+1
