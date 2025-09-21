class Solution:
    def minSplitMerge(self, a: List[int], b: List[int]) -> int:
        
        a,b,n=tuple(a),tuple(b),len(a)
        if a==b: return 0
        dq,vis=deque([a]),set([a])
        d=0

        while dq:
            for _ in range(len(dq)):
                a=dq.popleft()
                for l in range(n):
                    for r in range(l,n):
                        removed=a[l:r+1]
                        rem=a[:l]+a[r+1:]
                        for k in range(len(rem)):
                            if k==l: continue
                            cand=rem[:k]+removed+rem[k:]
                            if cand==b: return d+1
                            if cand in vis:continue
                            dq.append(cand);vis.add(cand)
            d+=1
        
        return -1