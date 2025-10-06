class Solution:
    def minSwaps(self, data: List[int]) -> int:
        tot = sum(data)
        cnt = sum(data[:tot])
        mx = cnt
        for i in range(tot, len(data)):
            cnt += data[i]
            cnt -= data[i - tot]
            mx = max(mx, cnt)
        return tot - mx