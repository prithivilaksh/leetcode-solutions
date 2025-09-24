class Solution:
    def firstDayBeenInAllRooms(self, next):
        n, M = len(next), 10**9 + 7
        dp = [0]*n
        for i in range(1, n):
            dp[i] = (dp[i-1] + 1 + (dp[i-1] - dp[next[i-1]]) + 1) % M

        return dp[-1]  

