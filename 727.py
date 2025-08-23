# Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

# If there is no such window in s1 that covers all characters in s2, return the empty string "".
# If there are multiple such minimum-length windows, return the one with the left-most starting index.


# Input: s1 = "abcdebdde", s2 = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of s2 in the window must occur in order.


# Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
# Output: ""

# Constraints:

# 1 <= s1.length <= 2 * 10^4
# 1 <= s2.length <= 100
# s1 and s2 consist of lowercase English letters.




# import sys
# sys.setrecursionlimit(100000) 
# from math import inf
# from functools import cache
# class Solution:
#     def minWindow(self, s1: str, s2: str) -> str:

#         l,res=inf,""
#         m,n=len(s1),len(s2)

#         @cache
#         def dp(i,j):
#             if j==n: return i-1
#             if i==m: return inf
            
#             end=dp(i+1,j)
#             if s1[i]==s2[j]: end=min(end,dp(i+1,j+1))
#             return end
        
#         dp(0,0)
#         for i in range(m):
#             end=dp(i,0)
#             if end != inf and end-i+1<l: l,res=end-i+1,s1[i:end+1]
#         return res


import sys
sys.setrecursionlimit(100000) ## just for testing.. not recommended
from math import inf
from functools import cache
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:

        l,res=inf,""
        m,n=len(s1),len(s2)

        @cache
        def dp(i,j):
            if j==n: return i-1
            if i==m: return inf 
            if s1[i]==s2[j]: return dp(i+1,j+1)
            return dp(i+1,j)
        
        for i in range(m):
            end=dp(i,0)
            if end != inf and end-i+1<l: l,res=end-i+1,s1[i:end+1]
        return res


# from math import inf
# from functools import cache
# class Solution:
#     def minWindow(self, s1: str, s2: str) -> str:

#         l,res=inf,""
#         m,n=len(s1),len(s2)

#         dp=[[inf]*(n+1) for i in range(m+1)]
#         for i in range(m+1): dp[i][n]=i
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if s1[i]==s2[j]: dp[i][j]=dp[i+1][j+1]
#                 else: dp[i][j]=dp[i+1][j]
                
#         for i in range(m):
#             end=dp[i][0]
#             end-=1
#             if end != inf and end-i+1<l: l,res=end-i+1,s1[i:end+1]
#         return res

# from math import inf
# from functools import cache
# class Solution:
#     def minWindow(self, s1: str, s2: str) -> str:

#         l,res=inf,""
#         m,n=len(s1),len(s2)

#         dp=[[inf]*(n+1) for i in range(m+1)]
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if s1[i]==s2[j]: dp[i][j]=i if j==n-1 else dp[i+1][j+1]
#                 else: dp[i][j]=dp[i+1][j]
                
#         for i in range(m):
#             end=dp[i][0]
#             if end != inf and end-i+1<l: l,res=end-i+1,s1[i:end+1]
#         return res

import time
if __name__ == "__main__":
    s=Solution()

    tests = [
    # Basic & given examples
    ("abcdebdde","bde","bcde"),
    ("abc","a","a"),
    ("jmeqksfrsdcmsiwvaovztaqenprpvnbstl","u",""),
    ("abcdebdde","de","de"),
    ("abcdbec","bec","bec"),
    ("abc","abc","abc"),
    ("axbxcxdx","abcd","axbxcxd"),
    ("abc","abcd",""),
    ("aaabaa","ba","ba"),
    ("a","a","a"),
    ("a","b",""),

    # Trickier overlaps
    ("cnhczmccqouqadqtmjjzl","mm","mccqouqadqtm"),   # multiple 'm'
    ("abdbcacb","acb","acb"),                       # multiple subsequences
    ("bbbacccab","cab","cab"),                      # overlap, leftmost chosen
    ("abcdbcde","bce","bcde"),                      # subsequence spanning overlap

    # Complex tricky subsequence placements
    ("abacbab","aab","abacb"),                      # multiple "a" choices
    ("xyzzzyx","zyx","zyx"),                       # overlapping reversed pattern
    ("hellotheregeneral","hrgne","heregene"),# s2 subseq not contiguous
    ("mississippi","issi","issi"),                  # multiple "issi", leftmost picked
    ("mississippi","sppi","sippi"),                # scattered subsequence
    ("qwertyqwerty","qty","qwerty"),                # multiple windows, choose leftmost

    # Edge stress
    ("z"*1000 + "abc" + "z"*1000, "abc", "abc"),  # long string, subseq in middle
    ("abc"*5000,"ac","abc"),                        # repeated pattern, shortest window
    ("a"*9999 + "b","ab","ab"),                     # match at the very end
    ]

    start_time = time.time()
    for s1, s2, expected in tests:
        result = s.minWindow(s1, s2)
        if result != expected:
            # print(f"FAIL: s.minWindow({s1!r}, {s2!r}) = {result!r}, expected {expected!r}")
            print(f"FAIL")
        else:
            # print(f"PASS: s.minWindow({s1!r}, {s2!r}) = {result!r}")
            print(f"PASS")
    print(f"Time: {time.time() - start_time}")





