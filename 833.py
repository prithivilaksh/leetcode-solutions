## testcases are wrong in few cases
class Solution:
    # def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
    #     s=list(s)
    #     off=0
    #     for i,p,q in sorted(zip(indices,sources,targets)):
            
    #         pl,ql=len(p),len(q)
    #         if s[off+i:off+i+pl]==list(p):
    #             s[off+i:off+i+pl]=q[:]
    #             off-=pl-ql
    #     return ''.join(s)

    # def findReplaceString(self, S, indexes, sources, targets):
    #     print(sorted(zip(indexes, sources, targets), reverse=True))
    #     for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
    #         S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
    #     return S

    def findReplaceString(self, S, indexes, sources, targets):
        res = list(S)
        for i, src, tar in zip(indexes, sources, targets):
            if S[i:i+len(src)] == src:
                res[i] = tar
                for j in range(i+1, i+len(src)): res[j] = '' 
        return ''.join(res)