class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 0, max(ribbons)
        while l < r:
            m = l+(r-l)//2
            cnt = sum(x//m for x in ribbons)
            if cnt >= k: l=m
            else: r=m-1
        return l