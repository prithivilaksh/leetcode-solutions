# Description
# You are given four integers minLength, maxLength, oneGroup and zeroGroup.

# A binary string is good if it satisfies the following conditions:

# The length of the string is in the range [minLength, maxLength].
# The size of each block of consecutive 1's is a multiple of oneGroup.
# For example in a binary string 00110111100 sizes of each block of consecutive ones are [2,4].
# The size of each block of consecutive 0's is a multiple of zeroGroup.
# For example, in a binary string 00110111100 sizes of each block of consecutive ones are [2,1,2].
# Return the number of good binary strings. Since the answer may be too large, return it modulo 109 + 7.

# Note that 0 is considered a multiple of all the numbers.

 

# Example 1:

# Input: minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2
# Output: 5
# Explanation: There are 5 good binary strings in this example: "00", "11", "001", "100", and "111".
# It can be proven that there are only 5 good strings satisfying all conditions.

# Example 2:

# Input: minLength = 4, maxLength = 4, oneGroup = 4, zeroGroup = 3
# Output: 1
# Explanation: There is only 1 good binary string in this example: "1111".
# It can be proven that there is only 1 good string satisfying all conditions.
 

# Constraints:

# 1 <= minLength <= maxLength <= 10^5
# 1 <= oneGroup, zeroGroup <= maxLength





# import sys
# sys.setrecursionlimit(10**6)
# from functools import cache
# class Solution:
#     def goodBinaryStrings(self, mi: int, mx: int, og: int, zg: int) -> int:

#         # idea/observation:
#         #     1) to find the count within range[mi,mx], we can find the count of length until mx and subtract count of length until mi
#         #     2) now the problem is to find the count <= length L
#         #     3) multiple of 1group or 0group means we can select 1 instance of minimum 1group and then either continue with 1group or 0group
#         #         eg if 1g is 2 and 0g is 3 then from 11, we can either go with 11+11 or 11+000
#         #     4) dp[l]=dp[l-1g]+dp[l-0g] // init dp[1g]+=1 and dp[0g]+=1

#         m=10**9+7
#         @cache
#         def dp(l):
#             if l==0: return 1
#             if l<0: return 0
#             return (dp(l-og)+dp(l-zg))%m
#         return sum(dp(i) for i in range(mi,mx+1))%m


class Solution:
    def goodBinaryStrings(self, mi: int, mx: int, og: int, zg: int) -> int:

        # idea/observation:
        #     1) to find the count within range[mi,mx], we can find the count of length until mx and subtract count of length until mi
        #     2) now the problem is to find the count <= length L
        #     3) multiple of 1group or 0group means we can select 1 instance of minimum 1group and then either continue with 1group or 0group
        #         eg if 1g is 2 and 0g is 3 then from 11, we can either go with 11+11 or 11+000
        #     4) dp[l]=dp[l-1g]+dp[l-0g] // init dp[1g]+=1 and dp[0g]+=1

        m=10**9+7
        dp=[0]*(mx+1)
        dp[0]=1
        for i in range(1,mx+1):
            if i-og>=0: dp[i]+=dp[i-og]
            if i-zg>=0: dp[i]+=dp[i-zg]
            dp[i]%=m
        return sum(dp[mi:])%m






print(Solution().goodBinaryStrings(2,3,1,2))
print(Solution().goodBinaryStrings(4,4,4,3))