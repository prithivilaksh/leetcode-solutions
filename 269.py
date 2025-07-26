class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # notes:
        #     abcd<abcda
        #     abcda<abcdb

        n=len(words)
        g=defaultdict(set)
        indeg={c:0 for word in words for c in word}
        for i in range(n-1):
            w1,w2=words[i],words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2): return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in g[w1[j]]: indeg[w2[j]]+=1
                    g[w1[j]].add(w2[j])
                    break
        
        res,q="",deque()
        for c in indeg:
            if indeg[c]==0: q.append(c)
        while q:
            u=q.popleft()
            res+=u
            for v in g[u]:
                indeg[v]-=1
                if indeg[v]==0: q.append(v)
        
        return res if len(res)==len(indeg) else ""





