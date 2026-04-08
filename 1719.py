class Solution:
    def checkWays(self,pairs):
        r = defaultdict(set)
        for x, y in pairs:
            r[x].add(y)
            r[y].add(x)

        n, mul = len(r), False
        ancestor = set()
        for x in sorted(r.keys(), key=lambda i: len(r[i]),reverse=True):
            p = min((r[x] & ancestor), key=lambda i: len(r[i]), default=0)  # find x's parent p
            ancestor.add(x)
            if p:
                if not r[x].issubset(r[p]|{p}): return 0
                mul |= len(r[p]) == len(r[x])
            elif len(r[x]) != n-1: return 0
        return 1 + mul
        