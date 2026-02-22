class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        candles,res=[],[]
        for i,c in enumerate(s):
            if c=="|": candles.append(i)
        
        for [l,r] in queries:
            l=bisect_left(candles,l)
            r=bisect_right(candles,r)-1
            if l<r: res.append(candles[r]-candles[l]-1 - (r-l-1))
            else: res.append(0)
        
        return res