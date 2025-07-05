# class Solution:
#     def findCoins(self, ways: List[int]) -> List[int]:
#         n = len(ways)
#         ways = [1] + ways
#         dp = [1] + [0] * n
#         res = []

#         for i in range(1, n + 1):
#             if dp[i] == ways[i]: continue

#             if ways[i] - dp[i] == 1:
#                 res.append(i)
#                 for j in range(i, n + 1):
#                     dp[j] += dp[j - i]

#             else: return []
#         return res


class Solution:
    def findCoins(self, dp: List[int]) -> List[int]:
        n = len(dp)
        dp = [1] + dp
        res = []
        for i in range(1, n + 1):
            if dp[i] == 0: continue
            if dp[i] != 1: return []
            res.append(i)
            for j in range(n, i - 1, -1):
                dp[j] -= dp[j - i]
                # if dp[j] < 0:return []
        return res