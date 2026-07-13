# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
        
#         def lcp(a,b):
#             n=min(len(a),len(b))
#             for i in range(n):
#                 if a[i]!=b[i]: return a[:i]
#             return a[:n]

#         res=strs[0]
#         for s in strs[1:]:
#             res=lcp(s,res)
#             if res=="":break
#         return res

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
        
#         def lcp(a,b):
#             n=min(len(a),len(b))
#             for i in range(n):
#                 if a[i]!=b[i]: return a[:i]
#             return a[:n]

#         strs.sort()
#         return lcp(strs[0],strs[-1])

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ml=min(len(s) for s in strs)
        for j in range(ml):
            for s in strs:
                if s[j]!=strs[0][j]: return s[:j]
        return strs[0][:ml]