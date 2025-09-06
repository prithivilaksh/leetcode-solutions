class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c2c,res=defaultdict(int),[0]
        for c in tiles: c2c[c]+=1
        def backtrack(c2c):
            res[0]+=1
            for k,v in c2c.items():
                if v:
                    c2c[k]-=1
                    backtrack(c2c)
                    c2c[k]+=1
        backtrack(c2c)
        return res[0]-1