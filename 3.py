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


